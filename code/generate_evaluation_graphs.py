import re
import json
import argparse
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
from typing import Dict, Optional

# Import the PDF parser
from pdf_parser import parse_evaluation_pdf

# --- Configuration ---
SCRIPT_DIR = Path(__file__).resolve().parent
CONFIG_PATH = SCRIPT_DIR / "config.json"

def load_config() -> dict:
    if not CONFIG_PATH.exists():
        print(f"Warning: Configuration file not found at {CONFIG_PATH}. Using defaults.")
        return {
            "evaluations_dir": "../teaching/evaluations",
            "output_graphs_dir": "../graphs"
        }
    with open(CONFIG_PATH, 'r') as f:
        return json.load(f)

config = load_config()
EVALUATIONS_DIR = (SCRIPT_DIR / config.get("evaluations_dir", "../teaching/evaluations")).resolve()
OUTPUT_GRAPHS_DIR = (SCRIPT_DIR / config.get("output_graphs_dir", "../graphs")).resolve()

# Only care about evaluations after 2017 Autumn
START_YEAR = 2017
START_QUARTER_ORDER = 3  # 0 for Winter, 1 for Spring, 2 for Summer, 3 for Autumn

# Mapping quarters to a numerical order for sorting
QUARTER_ORDER_MAP = {
    'WI': 0,
    'SP': 1,
    'S1': 1,
    'SU': 2,
    'AU': 3
}

def extract_metadata_from_filename(filename: str) -> Optional[Dict]:
    """
    Extracts year, quarter, and course code from a filename.
    Assumes format like 'Pisan-AU17-CSS343.pdf' or similar.
    """
    match = re.search(r'(AU|WI|SP|SU|S1|Autumn|Winter|Spring|Summer)(\d{2}|\d{4})[-_]([A-Z\s\-]+?\d{3})', filename, re.IGNORECASE)
    if not match:
        return None

    quarter_str = match.group(1).upper()
    year_str = match.group(2)
    course_code = match.group(3).upper().replace(" ", "").replace("-", "")

    year = int(year_str)
    if year < 100:
        year += 2000

    quarter_prefix = quarter_str[:2]
    if quarter_prefix == 'S1':
        quarter_prefix = 'SP'

    quarter_order = QUARTER_ORDER_MAP.get(quarter_prefix, -1)

    if quarter_order == -1:
        return None

    return {
        "year": year,
        "quarter": quarter_prefix,
        "quarter_order": quarter_order,
        "course_code": course_code
    }

def main():
    parser = argparse.ArgumentParser(description="Generate Teaching Evaluation Graphs")
    parser.add_argument("--start-year", type=int, default=START_YEAR, help="Start year for filtering evaluations")
    parser.add_argument("--course-filter", type=str, help="Course code to filter (e.g., CSS343)")
    args = parser.parse_args()

    OUTPUT_GRAPHS_DIR.mkdir(parents=True, exist_ok=True)

    error_log_path = OUTPUT_GRAPHS_DIR / "errors.log"
    with open(error_log_path, "w") as f:
        f.write("Evaluation Graph Generator Error Log\n")
        f.write("====================================\n")

    if not EVALUATIONS_DIR.exists():
        print(f"Evaluations directory not found: {EVALUATIONS_DIR}")
        return

    data = []
    for filepath in EVALUATIONS_DIR.glob("**/*.pdf"):
        metadata = extract_metadata_from_filename(filepath.name)
        if not metadata:
            continue

        if args.course_filter and metadata["course_code"] != args.course_filter:
            continue

        year = metadata["year"]
        q_order = metadata["quarter_order"]

        # Filter out anything before the specified start year
        if year < args.start_year:
            continue
        if args.start_year == START_YEAR and year == START_YEAR and q_order < START_QUARTER_ORDER:
            continue

        ratings = parse_evaluation_pdf(str(filepath))
        if not ratings or ratings.get("overall_summative_rating") is None or ratings.get("challenge_engagement_index") is None:
            with open(error_log_path, "a") as f:
                f.write(f"Unparseable or incomplete data in: {filepath.name}\n")
            continue

        data.append({
            "course_code": metadata["course_code"],
            "year": year,
            "quarter": metadata["quarter"],
            "quarter_order": q_order,
            "overall_summative_rating": ratings.get("overall_summative_rating"),
            "challenge_engagement_index": ratings.get("challenge_engagement_index")
        })

    if not data:
        print("No valid evaluation data found or extracted.")
        return

    df = pd.DataFrame(data)
    df = df.sort_values(by=["year", "quarter_order"])
    df["term"] = df["quarter"] + df["year"].astype(str).str[-2:]

    # Output a CSV/Excel Summary Report
    csv_output_path = OUTPUT_GRAPHS_DIR / "evaluations_summary.csv"
    df.to_csv(csv_output_path, index=False)
    print(f"Generated summary report: {csv_output_path}")

    grouped = df.groupby("course_code")
    generated_graphs = []

    for course, group in grouped:
        # Aggregate/Average in case there are multiple sections taught in the same term
        agg_df = group.groupby(["year", "quarter_order", "term"], as_index=False).mean(numeric_only=True)
        agg_df = agg_df.sort_values(by=["year", "quarter_order"])

        plt.figure(figsize=(10, 6))

        plt.plot(agg_df["term"], agg_df["overall_summative_rating"], marker='o', label='Overall Summative Rating (out of 5)')
        plt.plot(agg_df["term"], agg_df["challenge_engagement_index"], marker='s', label='Challenge & Engagement Index (out of 7)')

        plt.title(f"Teaching Evaluation Metrics Over Time: {course}")
        plt.xlabel("Term")
        plt.ylabel("Rating")
        plt.ylim(0, 7.5)  # Scale appropriately for both 5.0 and 7.0 scales
        plt.legend()
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.xticks(rotation=45)
        plt.tight_layout()

        output_path = OUTPUT_GRAPHS_DIR / f"{course}_evaluations.png"
        plt.savefig(output_path)
        plt.close()
        print(f"Generated graph for {course}: {output_path}")
        generated_graphs.append(output_path.name)

    # Generate HTML Dashboard
    html_content = [
        "<!DOCTYPE html>", "<html>", "<head>", "<title>Teaching Evaluation Dashboard</title>",
        "<style>body { font-family: sans-serif; margin: 40px; } a { color: #0066cc; text-decoration: none; } a:hover { text-decoration: underline; } img { max-width: 100%; height: auto; margin-bottom: 20px; } .graph-container { margin-bottom: 40px; border: 1px solid #ccc; padding: 20px; border-radius: 8px; }</style>",
        "</head>", "<body>", "<h1>Teaching Evaluation Dashboard</h1>",
        "<p><a href='evaluations_summary.csv'>Download Raw Data (CSV)</a></p>"
    ]
    for graph in sorted(generated_graphs):
        course_name = graph.replace('_evaluations.png', '')
        html_content.append(f"<div class='graph-container'><h2>{course_name}</h2><img src='{graph}' alt='Evaluation graph for {course_name}'></div>")
    html_content.append("</body>")
    html_content.append("</html>")

    html_output_path = OUTPUT_GRAPHS_DIR / "index.html"
    with open(html_output_path, "w") as f:
        f.write("\n".join(html_content))
    print(f"Generated dashboard: {html_output_path}")

if __name__ == "__main__":
    main()
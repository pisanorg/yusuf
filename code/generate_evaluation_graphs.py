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

    # Build per-course term list (with multi-section annotation) for the index
    term_section_counts = df.groupby(["course_code", "term", "year", "quarter_order"]).size().reset_index(name="sections")
    course_index = {}  # course_code -> list of (year, quarter_order, term_label)
    for _, row in term_section_counts.iterrows():
        # term is e.g. "AU25"; reconstruct as "2025AU"
        quarter = df.loc[df['term'] == row['term'], 'quarter'].iloc[0]
        label = f"{row['year']}{quarter}"
        if row["sections"] > 1:
            label += f"x{row['sections']}"
        course_index.setdefault(row["course_code"], []).append((row["year"], row["quarter_order"], label))
    for code in course_index:
        course_index[code].sort(key=lambda x: (x[0], x[1]))

    grouped = df.groupby("course_code")
    generated_graphs = []  # list of course_code strings

    for course, group in grouped:
        # Aggregate/Average in case there are multiple sections taught in the same term
        agg_df = group.groupby(["year", "quarter_order", "term"], as_index=False).mean(numeric_only=True)
        agg_df = agg_df.sort_values(by=["year", "quarter_order"])

        # Find terms with multiple sections to scatter individual points
        section_counts = group.groupby("term")["overall_summative_rating"].count()
        multi_section_terms = section_counts[section_counts > 1].index
        multi_df = group[group["term"].isin(multi_section_terms)]

        _, ax1 = plt.subplots(figsize=(10, 6))
        ax2 = ax1.twinx()

        color_osr = 'steelblue'
        color_cei = 'darkorange'

        ax1.plot(agg_df["term"], agg_df["overall_summative_rating"], marker='o', color=color_osr, label='Overall Summative Rating (out of 5)')
        ax2.plot(agg_df["term"], agg_df["challenge_engagement_index"], marker='s', color=color_cei, label='Challenge & Engagement Index (out of 7)')

        # Scatter individual section scores for terms with multiple sections
        if not multi_df.empty:
            ax1.scatter(multi_df["term"], multi_df["overall_summative_rating"], marker='o', color=color_osr, alpha=0.4, zorder=5, label='Individual Section (Overall)')
            ax2.scatter(multi_df["term"], multi_df["challenge_engagement_index"], marker='s', color=color_cei, alpha=0.4, zorder=5, label='Individual Section (Challenge & Engagement)')

        ax1.set_xlabel("Term")
        ax1.set_ylabel("Overall Summative Rating (out of 5)", color=color_osr)
        ax1.set_ylim(0, 5.5)
        ax1.tick_params(axis='y', labelcolor=color_osr)

        ax2.set_ylabel("Challenge & Engagement Index (out of 7)", color=color_cei)
        ax2.set_ylim(0, 7.7)
        ax2.tick_params(axis='y', labelcolor=color_cei)

        plt.title(f"Teaching Evaluation Metrics Over Time: {course}")
        ax1.set_xticks(range(len(agg_df["term"])))
        ax1.set_xticklabels(agg_df["term"], rotation=45)
        ax1.grid(True, linestyle='--', alpha=0.7)

        lines1, labels1 = ax1.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax1.legend(lines1 + lines2, labels1 + labels2, loc='lower left')

        plt.tight_layout()

        output_path = OUTPUT_GRAPHS_DIR / f"{course}_evaluations.png"
        plt.savefig(output_path)
        plt.close()
        print(f"Generated graph for {course}: {output_path}")
        generated_graphs.append(course)

    # Sort courses: by alpha prefix then by numeric course number
    def course_sort_key(code):
        m = re.match(r'([A-Z]+)(\d+)', code)
        return (m.group(1), int(m.group(2))) if m else (code, 0)

    sorted_courses = sorted(generated_graphs, key=course_sort_key)

    CSS = """
body { font-family: sans-serif; margin: 40px; max-width: 1200px; margin: 40px auto; }
h1 { border-bottom: 2px solid #333; padding-bottom: 10px; }
h2 { margin-top: 40px; }
a { color: #0066cc; text-decoration: none; }
a:hover { text-decoration: underline; }
ol.course-index { padding-left: 30px; line-height: 2; }
.thumbnail-grid { display: flex; flex-wrap: wrap; gap: 12px; margin-top: 20px; }
.thumbnail { width: calc(20% - 12px); min-width: 160px; text-align: center; }
.thumbnail img { width: 100%; height: auto; border: 1px solid #ccc; border-radius: 4px; }
.thumbnail p { margin: 4px 0 0; font-size: 0.85em; font-weight: bold; }
.graph-container { margin-bottom: 60px; border: 1px solid #ccc; padding: 20px; border-radius: 8px; scroll-margin-top: 20px; }
.graph-container img { max-width: 100%; height: auto; }
    """

    html_content = [
        "<!DOCTYPE html>", "<html>", "<head>",
        "<title>Teaching Evaluation Dashboard</title>",
        f"<style>{CSS}</style>",
        "</head>", "<body>",
        "<h1>Teaching Evaluation Dashboard</h1>",
        f"<h2>Courses Taught ({len(df)})</h2>",
        "<ol class='course-index'>",
    ]

    for course in sorted_courses:
        m = re.match(r'([A-Z]+)(\d+)', course)
        display_code = f"{m.group(1)} {m.group(2)}" if m else course
        terms = ", ".join(lbl for _, _, lbl in course_index.get(course, []))
        html_content.append(
            f"<li><a href='#{course}'>{display_code}</a> ({terms})</li>"
        )

    html_content += [
        "</ol>",
        "<h2>Overview</h2>",
        "<div class='thumbnail-grid'>",
    ]

    for course in sorted_courses:
        graph_file = f"{course}_evaluations.png"
        m = re.match(r'([A-Z]+)(\d+)', course)
        display_code = f"{m.group(1)} {m.group(2)}" if m else course
        html_content.append(
            f"<div class='thumbnail'><a href='#{course}'>"
            f"<img src='{graph_file}' alt='{display_code}'></a>"
            f"<p>{display_code}</p></div>"
        )

    html_content += ["</div>", "<h2>Detailed Graphs</h2>"]

    for course in sorted_courses:
        graph_file = f"{course}_evaluations.png"
        m = re.match(r'([A-Z]+)(\d+)', course)
        display_code = f"{m.group(1)} {m.group(2)}" if m else course
        html_content.append(
            f"<div class='graph-container' id='{course}'>"
            f"<h3>{display_code}</h3>"
            f"<img src='{graph_file}' alt='Evaluation graph for {display_code}'>"
            f"</div>"
        )

    html_content += [
        "<p><a href='evaluations_summary.csv'>Download Raw Data (CSV)</a></p>",
        "</body>", "</html>"
    ]

    html_output_path = OUTPUT_GRAPHS_DIR / "index.html"
    with open(html_output_path, "w") as f:
        f.write("\n".join(html_content))
    print(f"Generated dashboard: {html_output_path}")

if __name__ == "__main__":
    main()
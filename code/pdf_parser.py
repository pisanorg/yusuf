import re
from pypdf import PdfReader
from typing import Dict, Optional

def parse_evaluation_pdf(pdf_path: str) -> Dict[str, Optional[float]]:
    """
    Parses a PDF evaluation file and extracts the Overall Summative Rating
    and Challenge and Engagement Index (CEI). It searches all pages until
    both values are found.

    Args:
        pdf_path (str): The full path to the PDF file.

    Returns:
        dict: A dictionary containing 'overall_summative_rating' and
              'challenge_engagement_index'. Returns None for values if parsing fails.
    """
    result = {
        "overall_summative_rating": None,
        "challenge_engagement_index": None
    }

    try:
        reader = PdfReader(pdf_path)
        if not reader.pages:
            print(f"Warning: PDF '{pdf_path}' contains no pages.")
            return result

        # Define regex patterns
        summative_pattern = r'Overall Summative Rating[\s\S]*?(?:Median[\s\S]*?College Decile|Median)\s*([\d.]+)'
        cei_pattern = r'CEI:\s*([\d.]+)'

        for page in reader.pages:
            text = page.extract_text()
            if not text:
                continue

            # Extract Overall Summative Rating if not already found
            if result["overall_summative_rating"] is None:
                summative_match = re.search(summative_pattern, text, re.IGNORECASE)
                if summative_match:
                    result["overall_summative_rating"] = float(summative_match.group(1))

            # Extract Challenge and Engagement Index if not already found
            if result["challenge_engagement_index"] is None:
                cei_match = re.search(cei_pattern, text, re.IGNORECASE)
                if cei_match:
                    result["challenge_engagement_index"] = float(cei_match.group(1))

            # Break early if both are found
            if result["overall_summative_rating"] is not None and result["challenge_engagement_index"] is not None:
                break

        if result["overall_summative_rating"] is None or result["challenge_engagement_index"] is None:
            missing = []
            if result["overall_summative_rating"] is None:
                missing.append("Overall Summative Rating")
            if result["challenge_engagement_index"] is None:
                missing.append("Challenge and Engagement Index (CEI)")
            print(f"Warning: Failed to extract {', '.join(missing)} from '{pdf_path}' after searching {len(reader.pages)} pages.")

    except Exception as e:
        print(f"Error parsing PDF '{pdf_path}': {e}")

    return result
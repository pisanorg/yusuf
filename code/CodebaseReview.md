# Codebase Review and Architecture

This document outlines how the Evaluation Graph Generator functions and how data flows through the application.

## Overview

The codebase is separated into three main files:
1. **`generate_evaluation_graphs.py`**: The orchestrator.
2. **`pdf_parser.py`**: The extraction engine.
3. **`config.json`**: The environmental variables.

## Data Flow

1. **Initialization:** `generate_evaluation_graphs.py` begins by resolving paths against `config.json`. It guarantees the output `graphs` folder exists.
2. **File Discovery:** Using `pathlib.Path.glob`, it recursively maps all PDF files located in the target directory (`../teaching/evaluations`).
3. **Metadata Extraction:** For each discovered PDF, the `extract_metadata_from_filename()` function parses the filename (e.g. `Pisan-AU17-CSS132A.pdf`) via regular expressions to deduce:
   * Year (`2017`)
   * Quarter (`Autumn`, order index: `3`)
   * Course Code (`CSS132A`)
4. **Date Filtering:** The orchestrator checks if the evaluation is $\ge$ Autumn 2017. If not, it skips it.
5. **PDF Parsing:** Validated files are passed to `pdf_parser.py`.
   * The `pypdf` library extracts plaintext from the pages sequentially until the metrics are found.
   * Regular expressions isolate the numbers following the `Overall Summative Rating ... Median College Decile` columns, as well as the `CEI:` parameter.
6. **Data Structuring:** Values are appended to a flat list of dictionaries, which is subsequently converted into a `pandas.DataFrame`.
7. **Aggregation:** In instances where multiple sections of the same course are taught in the exact same quarter, the DataFrame groups these overlaps and takes a numerical `.mean()` average of the scores.
8. **Visualization:** The dataset is grouped by `course_code`. For each course, `matplotlib` constructs a line chart with two series plotted against a synchronized chronological axis (`Term`). The Y-axis is scaled from 0 to 7.5 to accommodate both 5-point and 7-point systems.
9. **Export:** Images are dumped to the `../graphs` directory as `<COURSE_CODE>_evaluations.png`.
10. **Dashboard Generation:** An `index.html` file is generated in the `../graphs` directory, embedding all the output images into a single web page.

## Maintenance Notes
* **Regex Drift:** If the university switches evaluation formats away from IASystem or changes the PDF layout, `pdf_parser.py`'s regular expressions will be the single point of failure and will require adjustment.
* **Scale Changes:** The graphing component (`generate_evaluation_graphs.py`) hardcodes the Y-axis limit to `7.5` to visually support both 5-point and 7-point scales simultaneously. If the university evaluation scales change in the future, this limit will need to be updated.
* **Path Assumptions:** The configuration assumes relative folder structures. If this `code` folder is moved elsewhere in the repository, `config.json` must be updated.
* **Chronological Sorting:** Quarters are hardcoded to a specific sorting order (WI=0, SP=1, SU=2, AU=3) within the `QUARTER_ORDER_MAP` to ensure graphs flow chronologically. Adjust this mapping if the academic calendar hierarchy changes.
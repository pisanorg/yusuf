# Teaching Evaluation Graph Generator

This tool automates the extraction of teaching evaluation metrics (Overall Summative Rating and Challenge & Engagement Index) from historical IASystem PDF reports and visualizes them over time using line graphs.

## Prerequisites

Ensure you have Python 3.8+ installed on your system.

## Expected File Naming Convention

The orchestrator relies on file names to extract the term and course information. Files should be named with a format resembling `*-[Quarter][Year]-[CourseCode].pdf` (e.g., `Pisan-AU17-CSS132A.pdf` or `Pisan-WI20-CSS343B.pdf`).

*Note: The script will automatically group and average the evaluation scores if multiple sections of the exact same course are taught in the same term (e.g., CSS343A and CSS343B in AU25).*

## Environment Setup

To keep this project portable and avoid conflict with your global Python packages, it is recommended to run this inside a virtual environment.

1. **Navigate to the `code` directory:**
   ```bash
   cd /Users/pisan/bitbucket/pisanorg/yusuf/code/
   ```

2. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   ```

3. **Activate the virtual environment:**
   ```bash
   source venv/bin/activate
   ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Configuration & Usage

The directories for your evaluations and graphs are stored in `config.json`. By default, they point to relative paths (`../teaching/evaluations` and `../graphs`).

To generate or update the graphs, simply run:
```bash
python generate_evaluation_graphs.py
```
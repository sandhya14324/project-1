# Student Performance Analysis System

A complete data analysis project using **MySQL + Python + Excel** — analyzing exam performance of 1,000 students across Math, Reading, and Writing to uncover pass/fail trends, gender-based differences, and the impact of test preparation.

## Tools Used
Python · Pandas · NumPy · MySQL · MS Excel

## What This Project Does
- Loads student exam data into MySQL and queries it with **6 SQL queries** covering `AVG`, `SUM`/`CASE WHEN`, `ORDER BY`, `GROUP BY`, and `CREATE VIEW`
- Connects to MySQL from Python, analyzes the data with **Pandas** and **NumPy** (mean, median, std dev, percentile rankings)
- Exports results to a multi-sheet **Excel workbook** with a dashboard: subject averages, pass/fail rates, gender comparison, and top/bottom performers

## Key Findings
- Identified which subject has the lowest average score
- Found the overall pass rate and pass/fail split per subject
- Compared male vs female average performance
- Measured the score impact of completing the test preparation course
- Ranked top 10 and bottom 10 performers by total score

## Setup — After Cloning This Repo

1. **Clone the repo**
   ```
   git clone <your-repo-url>
   cd student-performance-analysis
   ```

2. **Get the dataset**
   Download `StudentsPerformance.csv` from Kaggle — [Students Performance in Exams](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams). Put the CSV in this same folder (not included in repo).

3. **Set up MySQL**
   Open MySQL Workbench → connect to your local instance → run:
   ```sql
   CREATE DATABASE student_analysis;
   USE student_analysis;
   ```
   Then: right-click `student_analysis` in the left panel → **Table Data Import Wizard** → select `StudentsPerformance.csv` → table name `students` → Next → Next → Finish.

4. **Run the SQL queries**
   Open `queries.sql` in MySQL Workbench, select all, click the lightning bolt ⚡ to run.

5. **Install Python packages**
   ```
   pip install -r requirements.txt
   ```

6. **Set your MySQL credentials**
   Open `analysis.py`, edit these lines with your own MySQL username/password:
   ```python
   user="root",
   password="your_password_here",
   ```

7. **Run the analysis**
   ```
   python analysis.py
   ```
   Creates `student_analysis_results.xlsx` with 5 sheets (data + stats).

8. **Build the dashboard**
   ```
   python build_dashboard.py
   ```
   Adds a `DASHBOARD` sheet to the Excel file with 4 charts + summary boxes.

9. **Take a screenshot**
   Open `student_analysis_results.xlsx` → go to the DASHBOARD sheet → screenshot it → save as `dashboard_screenshot.png` for your resume/portfolio.

## Files
| File | Purpose |
|---|---|
| `queries.sql` | 6 MySQL queries — averages, pass/fail, top 10, gender comparison, test prep impact, high-scorers view |
| `analysis.py` | Connects to MySQL, analyzes data with Pandas/NumPy, exports to Excel |
| `build_dashboard.py` | Adds a DASHBOARD sheet with charts + summary stats to the Excel output |
| `StudentsPerformance.csv` | Raw dataset (not included — download from Kaggle) |
| `student_analysis_results.xlsx` | Generated output (not included — created by running the scripts) |

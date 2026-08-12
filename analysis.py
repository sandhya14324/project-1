"""
Student Performance Analysis
Connects to MySQL, analyzes exam data with Pandas + NumPy,
and exports results to an Excel file with multiple sheets.
"""

import mysql.connector
import pandas as pd
import numpy as np

# 1. Connect to MySQL and load data
# Replace with your own MySQL username/password (the one you set in MySQL Workbench)
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password_here",
    database="student_analysis"
)

df = pd.read_sql("SELECT * FROM students", conn)
conn.close()

# 2. Calculate total score and rank
df["total_score"] = df["math score"] + df["reading score"] + df["writing score"]
df["rank"] = df["total_score"].rank(ascending=False, method="min").astype(int)
df = df.sort_values("rank").reset_index(drop=True)

# 3. Subject-wise statistics (mean, median, max, min) using NumPy
subjects = ["math score", "reading score", "writing score"]
stats_rows = []
for subject in subjects:
    scores = df[subject].to_numpy()
    stats_rows.append({
        "subject": subject,
        "mean": np.mean(scores),
        "median": np.median(scores),
        "max": np.max(scores),
        "min": np.min(scores),
        "std_dev": np.std(scores),
        "pct_above_70": np.mean(scores > 70) * 100,
    })
stats_df = pd.DataFrame(stats_rows)

# 4. Gender comparison
gender_df = df.groupby("gender")[subjects + ["total_score"]].mean().reset_index()

# 5. Top 10 and Bottom 10 students
top10 = df.nsmallest(10, "rank")[
    ["gender", "race/ethnicity", "math score", "reading score", "writing score", "total_score", "rank"]
]
bottom10 = df.nlargest(10, "rank")[
    ["gender", "race/ethnicity", "math score", "reading score", "writing score", "total_score", "rank"]
]
top_bottom_df = pd.concat(
    [top10.assign(group="Top 10"), bottom10.assign(group="Bottom 10")]
)

# 6. Test preparation impact
prep_df = df.groupby("test preparation course")[subjects + ["total_score"]].mean().reset_index()

# 7. Export everything to Excel with separate sheets
with pd.ExcelWriter("student_analysis_results.xlsx", engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="All Data", index=False)
    stats_df.to_excel(writer, sheet_name="Subject Stats", index=False)
    gender_df.to_excel(writer, sheet_name="Gender Comparison", index=False)
    top_bottom_df.to_excel(writer, sheet_name="Top10 Bottom10", index=False)
    prep_df.to_excel(writer, sheet_name="Test Prep Impact", index=False)

print("Done. Exported to student_analysis_results.xlsx")
print(f"Total students: {len(df)}")
print(f"Overall pass rate (>=40 all subjects): "
      f"{((df[subjects] >= 40).all(axis=1).mean() * 100):.1f}%")
print(f"Highest total score: {df['total_score'].max()}")
print("Subject with lowest average:", stats_df.loc[stats_df['mean'].idxmin(), 'subject'])

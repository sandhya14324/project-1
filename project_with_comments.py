"""
Student Performance Analysis
Connects to MySQL,analyzes exam data data with Pandas+Numpy,
and exports result to an Excel file with Multiple Sheets.
"""
import mysql.connector 
import numpy as np                 
import pandas as pd               
             
# 1.Connect to MySQL Database

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sandhya@1402",
    database="student_analysis"
)

print("Connection established successfully!")

# Create cursor object
cursor = conn.cursor()
cursor.execute("show tables")
# ==========================================================
# 1. Calculate Total Marks of Each Student
# ==========================================================
cursor.execute("""
SELECT (`math score` + `reading score` + `writing score`) AS total_score
FROM students
""")
total_marks = cursor.fetchall()
print("Total Marks of Students")
print(total_marks)

# ==========================================================
# 2. Rank Students Based on Total Marks
# ==========================================================
cursor.execute("""
SELECT
(`math score` + `reading score` + `writing score`) AS total_score,
DENSE_RANK() OVER (
ORDER BY (`math score` + `reading score` + `writing score`) DESC
) AS student_rank
FROM students""")
rank = cursor.fetchall()
print("\nStudent Ranking")
for row in rank:
    print(row)

# ==========================================================
# 3. Find Mean, Maximum, Minimum and Median
# ==========================================================
df = pd.read_sql("SELECT * FROM students", conn)
# mean
print("Math Mean:", np.mean(df["math score"]))
print("Reading Mean:", np.mean(df["reading score"]))
print("Writing Mean:", np.mean(df["writing score"]))

cursor.execute("""
SELECT MAX(`math score`), MAX(`reading score`), MAX(`writing score`)
FROM students
""")
print("maximum score",cursor.fetchall())

cursor.execute("""
SELECT MIN(`math score`), MIN(`reading score`), MIN(`writing score`)
FROM students
""")
print("minimum score",cursor.fetchall())
# median
print("Math Median:", np.median(df["math score"]))
print("Reading Median:", np.median(df["reading score"]))
print("Writing Median:", np.median(df["writing score"]))

# ==========================================================
# 4. Percentage of Students Scoring Above 70
# ==========================================================
cursor.execute("""SELECT
(COUNT(CASE WHEN `math score` > 70 THEN 1 END) * 100.0 / COUNT(*)) AS math_percentage,
(COUNT(CASE WHEN `reading score` > 70 THEN 1 END) * 100.0 / COUNT(*)) AS reading_percentage,
(COUNT(CASE WHEN `writing score` > 70 THEN 1 END) * 100.0 / COUNT(*)) AS writing_percentage
FROM students""")
result = cursor.fetchone()
print(result)
# print("\nPercentage Above 70")
print("Math:", float(result[0]), "%")
print("Reading:", float(result[1]), "%")
print("Writing:", float(result[2]), "%")

# ==========================================================
# 5. Average Total Score by Gender
# ==========================================================
cursor.execute("""SELECT gender,
AVG(`math score` + `reading score` + `writing score`) AS avg_score
FROM students
GROUP BY gender""")
# print("\nAverage Total Score by Gender")
print(cursor.fetchall())

# ==========================================================
# 6. Compare Scores by Test Preparation Course
# ==========================================================
myquery = """
SELECT `test preparation course`,
AVG(`math score`) AS avg_math,
AVG(`reading score`) AS avg_reading,
AVG(`writing score`) AS avg_writing
FROM students
GROUP BY `test preparation course`
"""
comparison = pd.read_sql(myquery, conn)
print("\nAverage Scores Based on Test Preparation Course"),print(comparison)
# Close database resources
cursor.close()
conn.close()


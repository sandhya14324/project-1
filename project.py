import numpy as np
import pandas as pd
import mysql.connector 
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="sandhya@1402",
    database="student_analysis"
)
print("connection done")
cursor=conn.cursor()
# 1.total marks of student
cursor.execute("""SELECT (`math score`+`reading score`+`writing score`) AS 'total score'
FROM students""")
total_marks=cursor.fetchall()
print(total_marks)
# 2.rank students on total score
cursor.execute("""SELECT
(`math score` + `reading score` + `writing score`) AS total_score,
DENSE_RANK() OVER (
ORDER BY (`math score` + `reading score` + `writing score`) DESC
) AS student_rank
FROM students""")
rank=cursor.fetchall()
for row in rank:
     print("Total Marks:", row[0], "Rank:", row[1])
# 3.find mean,meadin,max,min score for each subject
df = pd.read_sql("SELECT * FROM students", conn)
print(np.mean(df["math score"]))
print(np.mean(df["reading score"]))
print(np.mean(df["writing score"]))
# max
cursor.execute("""SELECT max(`math score`),max(`reading score`),max(`writing score`)
FROM students""")
highest=cursor.fetchall()
print(highest)
# min
cursor.execute("""SELECT min(`math score`),min(`reading score`),min(`writing score`)
FROM students""")
lowest=cursor.fetchall()
print(lowest)
# median
df = pd.read_sql("SELECT * FROM students", conn)
print("math median",np.median(df["math score"]))
print("reading median",np.median(df["reading score"]))
print("writing median",np.median(df["writing score"]))
# 4. Find what % of students scored above 70 in each subject
cursor.execute("""SELECT
    (COUNT(CASE WHEN `math score` > 70 THEN 1 END) * 100.0 / COUNT(*)) AS math_percentage,
    (COUNT(CASE WHEN `reading score` > 70 THEN 1 END) * 100.0 / COUNT(*)) AS reading_percentage,
    (COUNT(CASE WHEN `writing score` > 70 THEN 1 END) * 100.0 / COUNT(*)) AS writing_percentage
FROM students""")
result = cursor.fetchone()
print(float(result[0]))
print(float(result[1]))
print(float(result[2]))
# 5.Group by gender and find average total score
cursor.execute("""SELECT gender,avg(`math score`+`reading score`+`writing score`) 'avg_score'
FROM students
GROUP BY gender""")
print(cursor.fetchall())
# 6.check if students who completed test prep scored higher(yes/no comparision)
myquery="""SELECT `test preparation course`,
avg(`math score`) "avg_math",
avg(`reading score`) "avg_reading",
avg(`writing score`) "avg_writin"
FROM students
GROUP BY `test preparation course`"""
comparision=pd.read_sql(myquery,conn)
print(comparision)




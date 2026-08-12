-- Student Performance Analysis — MySQL Queries
-- Database setup
CREATE DATABASE IF NOT EXISTS student_analysis;
USE student_analysis;

-- Query 1: Average score per subject
SELECT 'Math' AS subject, AVG(`math score`) AS average_score FROM students
UNION
SELECT 'Reading', AVG(`reading score`) FROM students
UNION
SELECT 'Writing', AVG(`writing score`) FROM students;

-- Query 2: Pass/Fail count (pass = score above 40)
SELECT
  SUM(CASE WHEN `math score` >= 40 THEN 1 ELSE 0 END) AS math_pass,
  SUM(CASE WHEN `math score` < 40 THEN 1 ELSE 0 END) AS math_fail,
  SUM(CASE WHEN `reading score` >= 40 THEN 1 ELSE 0 END) AS reading_pass,
  SUM(CASE WHEN `reading score` < 40 THEN 1 ELSE 0 END) AS reading_fail
FROM students;

-- Query 3: Top 10 students by total score
SELECT gender, (`math score` + `reading score` + `writing score`) AS total_score
FROM students
ORDER BY total_score DESC
LIMIT 10;

-- Query 4: Gender-wise average score
SELECT gender,
  AVG(`math score`) AS avg_math,
  AVG(`reading score`) AS avg_reading,
  AVG(`writing score`) AS avg_writing
FROM students
GROUP BY gender;

-- Query 5: Test preparation impact
SELECT `test preparation course`,
  AVG(`math score`) AS avg_math,
  AVG(`reading score`) AS avg_reading
FROM students
GROUP BY `test preparation course`;

-- Query 6: View for high scorers (total > 240)
CREATE OR REPLACE VIEW high_scorers AS
SELECT *, (`math score` + `reading score` + `writing score`) AS total
FROM students
WHERE (`math score` + `reading score` + `writing score`) > 240;

SELECT * FROM high_scorers;

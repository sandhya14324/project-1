-- STUDENT PERFORMANCE ANALYSIS
-- MySQL Queries
-- STEP 1: Create the database
-- Create a database called student_analysis
CREATE DATABASE student_analysis;

-- Select the database so that we can work inside it
USE student_analysis;

-- QUERY 1: Average score for each subject
-- AVG() calculates the average score.
-- Here we calculate the average for:
-- 1. Math
-- 2. Reading
-- 3. Writing
--
-- UNION combines the three results into one table.

SELECT 'Math' AS subject,avg(`math score`) as average_score
FROM students
UNION
SELECT 'Reading' AS subject,avg(`reading score`) 
FROM students
UNION
SELECT 'writing' AS subject,avg(`writing score`)
FROM students;

-- QUERY 2: Pass and Fail count for each subject
-- Passing score is 40 or above.
--
-- CASE WHEN checks whether the student's score is
-- greater than or equal to 40.
--
-- SUM() counts how many students satisfy the condition.
--
-- We calculate pass and fail for all three subjects.

SELECT
SUM(CASE WHEN `math score` >= 40 THEN 1 ELSE 0 END) AS math_pass,
SUM(CASE WHEN `math score` < 40 THEN 1 ELSE 0 END) AS math_fail,

SUM(CASE WHEN `reading score` >= 40 THEN 1 ELSE 0 END) AS reading_pass,
SUM(CASE WHEN `reading score` < 40 THEN 1 ELSE 0 END) AS reading_fail,

SUM(CASE WHEN `writing score` >= 40 THEN 1 ELSE 0 END) AS writing_pass,
SUM(CASE WHEN `writing score` < 40 THEN 1 ELSE 0 END) AS writing_fail
FROM students;

-- QUERY 3: Top 10 students by total score
-- Total score = Math + Reading + Writing.
--
-- ORDER BY sorts the students from highest
-- total score to lowest.
--
-- LIMIT 10 gives only the top 10 students.

SELECT gender,(`math score`+`reading score`+`writing score`) AS total_score
FROM students
ORDER BY total_score DESC
LIMIT 10;

-- QUERY 4: Gender-wise average score
-- GROUP BY gender creates separate groups
-- for male and female students.
--
-- AVG() calculates the average score
-- for each gender.

SELECT gender,
avg(`math score`) as avg_math,
avg(`reading score`) as avg_reading,
avg(`writing score`) as avg_writing
FROM students
GROUP BY gender;

-- QUERY 5: Test preparation impact
-- We compare students who completed the
-- test preparation course with those who did not.
--
-- GROUP BY creates separate groups based on
-- the test preparation course.
--
-- AVG() calculates the average score for each group.


SELECT `test preparation course`,
avg(`math score`) AS avg_math,
avg(`reading score`) AS avg_reading
FROM students
group by `test preparation course`;

-- QUERY 6: Create a view for high scorers
-- A VIEW is a saved SQL query.
--
-- Here we create a view called high_scorers.
--
-- Students whose total score is greater than 240
-- will be included in this view.

CREATE VIEW high_scorers AS
SELECT *,(`math score`+`reading score`+`writing score`) AS total
FROM students
WHERE (`math score`+`reading score`+`writing score`)>240;
select * from high_scorers;


WITH
    first_score AS (
        SELECT
            student_id
            , subject
            , LAG(score) OVER (PARTITION BY student_id, subject ORDER BY exam_date) AS first_score
            , score AS latest_score
        FROM Scores
    )

SELECT *
FROM first_score
WHERE first_score < latest_score
ORDER BY student_id, subject

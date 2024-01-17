WITH join_experience_years AS (
    SELECT
        p.project_id
        , p.employee_id
        , CAST(e.experience_years AS FLOAT) AS experience_years
    FROM Project p
    LEFT JOIN Employee e
    ON p.employee_id = e.employee_id
)

SELECT
    project_id
    , ROUND(AVG(experience_years), 2) AS average_years
FROM join_experience_years
GROUP BY project_id

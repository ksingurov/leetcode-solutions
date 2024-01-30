WITH managers AS (
    SELECT
        reports_to AS employee_id
        , COUNT(*) AS reports_count
        , ROUND(AVG(CAST(age AS FLOAT)), 0) AS average_age
    FROM Employees
    WHERE reports_to IS NOT NULL
    GROUP BY reports_to
)

SELECT
    m.employee_id
    , e.name
    , m.reports_count
    , m.average_age
FROM managers m
LEFT JOIN Employees e
ON m.employee_id = e.employee_id
ORDER BY m.employee_id

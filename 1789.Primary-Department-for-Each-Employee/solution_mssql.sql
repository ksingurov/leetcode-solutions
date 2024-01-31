WITH row_n AS (
    SELECT
        employee_id
        , department_id
        , ROW_NUMBER() OVER (PARTITION BY employee_id ORDER BY primary_flag DESC) AS row_n
    FROM Employee
)

SELECT
    employee_id
    , department_id
FROM row_n
WHERE row_n = 1

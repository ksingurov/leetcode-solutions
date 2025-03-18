-- Page on Microsoft Learn:
-- Use a recursive common table expression to display multiple levels of recursion:
-- https://learn.microsoft.com/en-us/sql/t-sql/queries/with-common-table-expression-transact-sql?view=sql-server-ver16#d-use-a-recursive-common-table-expression-to-display-multiple-levels-of-recursion


WITH cte_levels AS (
    SELECT
        employee_id
        , employee_name
        , manager_id
        , 1 AS level
    FROM Employees
    WHERE manager_id IS NULL

    UNION ALL

    SELECT
        e.employee_id
        , e.employee_name
        , e.manager_id
        , l.level + 1 AS level
    FROM Employees e
    INNER JOIN cte_levels l ON e.manager_id = l.employee_id
)

SELECT *
FROM cte_levels
ORDER BY level
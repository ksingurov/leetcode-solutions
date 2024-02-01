WITH all_employee_ids AS (
    SELECT employee_id FROM Employees
    UNION
    SELECT employee_id FROM Salaries
)

SELECT
    all_.employee_id
FROM all_employee_ids all_
LEFT JOIN Employees emp
    ON all_.employee_id = emp.employee_id
LEFT JOIN Salaries sal
    ON all_.employee_id = sal.employee_id
WHERE emp.name IS NULL OR sal.salary IS NULL
ORDER BY employee_id

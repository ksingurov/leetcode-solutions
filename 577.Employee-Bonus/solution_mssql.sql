SELECT
    emp.name
    , bon.bonus
FROM Employee emp
LEFT JOIN Bonus bon
ON emp.empId = bon.empId
WHERE COALESCE(bon.bonus, 0) < 1000

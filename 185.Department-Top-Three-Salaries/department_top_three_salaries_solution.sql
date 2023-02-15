WITH rank_table AS (
    SELECT 
          name
        , salary
        , departmentId
        , DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS rank_n
    FROM Employee
)

SELECT
      rt.name   AS Employee
    , d.name    AS Department
    , rt.salary AS Salary
FROM rank_table rt
LEFT JOIN Department d
    ON rt.departmentId = d.id
WHERE rt.rank_n <= 3;
-- with subquery instead of CTE
-- beats ~7% (the worst solution so far)

DELETE FROM Person
WHERE EXISTS (
    SELECT 1
    FROM (
        SELECT
            id
            , ROW_NUMBER() OVER (PARTITION BY email ORDER BY id) AS row_n
        FROM Person
    ) AS row_n
    WHERE row_n.row_n > 1
      AND row_n.id = Person.id
)

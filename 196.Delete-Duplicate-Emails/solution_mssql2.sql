-- safe (NULLs are not a problem)
-- beats ~13%

WITH row_n AS (
    SELECT
        id
        , ROW_NUMBER() OVER (PARTITION BY email ORDER BY id) AS row_n
    FROM Person
)

DELETE FROM Person
WHERE NOT EXISTS (
    SELECT 1 FROM row_n r WHERE r.row_n = 1 AND r.id = Person.id
)

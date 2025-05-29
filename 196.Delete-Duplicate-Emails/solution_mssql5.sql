-- with EXISTS
-- beats ~75% (best solution so far)

WITH
    row_n AS (
        SELECT
            id
            , ROW_NUMBER() OVER (PARTITION BY email ORDER BY id) AS row_n
        FROM Person
    )

DELETE FROM Person
WHERE EXISTS (
    SELECT id FROM row_n rn WHERE rn.row_n > 1 AND rn.id = Person.id
)

-- beats ~13%

WITH
    row_n AS (
        SELECT
            id
            , ROW_NUMBER() OVER (PARTITION BY email ORDER BY id) AS row_n
        FROM Person
    )

DELETE FROM Person
WHERE id NOT IN (
    SELECT id FROM row_n WHERE row_n = 1

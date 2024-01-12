WITH all_single_numbers AS (
    SELECT
        num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(*) = 1
)

SELECT
    MAX(num) AS num
FROM all_single_numbers

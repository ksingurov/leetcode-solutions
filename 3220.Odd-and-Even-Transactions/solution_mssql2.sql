-- solutiton with PIVOT

WITH
    odd_even AS (
        SELECT
            *
            , IIF(amount % 2 = 1, 'odd_sum', 'even_sum') AS odd_even
        FROM transactions
    )
    , group_by AS (
        SELECT
            transaction_date
            , odd_even
            ,SUM(amount) AS amount
        FROM odd_even
        GROUP BY transaction_date, odd_even
    )

SELECT 
    transaction_date
    , ISNULL(odd_sum, 0) AS odd_sum
    , ISNULL(even_sum, 0) AS even_sum
FROM group_by
PIVOT (
    SUM(amount)
    FOR odd_even IN ("odd_sum", "even_sum")
) AS PivotTable

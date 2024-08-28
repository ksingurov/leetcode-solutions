WITH odd_even AS (
    SELECT
        *
        , amount % 2 AS odd_transaction
    FROM transactions
)

SELECT
    transaction_date
    , SUM(IIF(odd_transaction = 1, amount, 0)) AS odd_sum
    , SUM(IIF(odd_transaction = 0, amount, 0)) AS even_sum
FROM odd_even
GROUP BY transaction_date
ORDER BY transaction_date

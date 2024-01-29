WITH balance AS (
    SELECT
        account
        , SUM(amount) AS balance
    FROM Transactions
    GROUP BY account
)

SELECT
    u.name
    , b.balance
FROM balance b
LEFT JOIN Users u
ON b.account = u.account
WHERE b.balance > 10000

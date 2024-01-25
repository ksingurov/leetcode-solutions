WITH customer_ids_with_no_transactions AS (
    SELECT
        v.customer_id
    FROM Visits v
    LEFT JOIN Transactions t
    ON v.visit_id = t.visit_id
    WHERE t.transaction_id IS NULL
)

SELECT
    customer_id
    , COUNT(*) AS count_no_trans
FROM customer_ids_with_no_transactions
GROUP BY customer_id

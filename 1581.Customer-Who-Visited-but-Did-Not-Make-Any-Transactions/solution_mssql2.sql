-- with NOT EXISTS

WITH customer_ids_with_no_transactions AS (
    SELECT
        v.customer_id
    FROM Visits v
    WHERE NOT EXISTS (
        SELECT 1
        FROM Transactions t
        WHERE v.visit_id = t.visit_id
    )
)

SELECT
    customer_id
    , COUNT(*) AS count_no_trans
FROM customer_ids_with_no_transactions
GROUP BY customer_id

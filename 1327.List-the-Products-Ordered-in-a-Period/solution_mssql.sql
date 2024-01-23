WITH units_ordered AS (
    SELECT
        product_id
        , SUM(unit) AS unit
    FROM Orders
    WHERE YEAR(order_date) = 2020 AND MONTH(order_date) = 2
    GROUP BY product_id
)

SELECT
    p.product_name
    , u.unit
FROM units_ordered u
LEFT JOIN Products p
    ON u.product_id = p.product_id
WHERE u.unit >= 100

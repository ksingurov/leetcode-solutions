-- commeents:
-- interesting problem compared to other Medium ones: compose a post and a description
-- step 1: calculate valid product pairs: it is ensured by INNER JOIN and p1.product_id < p2.product_id
-- step2: counts
-- step3: final table


WITH
    product_pairs AS (
        SELECT
            p1.user_id
            , p1.product_id AS product1_id
            , p2.product_id AS product2_id
        FROM ProductPurchases p1
        INNER JOIN ProductPurchases p2
            ON p1.user_id = p2.user_id
            AND p1.product_id < p2.product_id
    )
    , count_product_pairs AS (
        SELECT
            product1_id
            , product2_id
            , COUNT(*) AS customer_count
        FROM product_pairs
        GROUP BY product1_id, product2_id
    )

SELECT
    c.product1_id
    , c.product2_id
    , info1.category AS product1_category
    , info2.category AS product2_category
    , c.customer_count
FROM count_product_pairs c
LEFT JOIN ProductInfo info1 ON c.product1_id = info1.product_id
LEFT JOIN ProductInfo info2 ON c.product2_id = info2.product_id
WHERE c.customer_count >= 3
ORDER BY c.customer_count DESC, c.product1_id, c.product2_id

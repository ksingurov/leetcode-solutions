-- it is a "follow-up" of problem 3521
-- in contrast to problem 3521, some products may belong to similar categories
-- since we need to find product pairs from different categories, we need to use the ProductInfo table
-- join ProductInfo and select the distinct pairs of categories
-- then follow the same logic as problem 3521

WITH
    purchased_categories AS (
        SELECT DISTINCT
            purchases.user_id
            , info.category
        FROM ProductPurchases purchases
        LEFT JOIN ProductInfo info
            ON purchases.product_id = info.product_id
    )
    , categories_pairs AS (
        SELECT
            cat1.user_id
            , cat1.category AS category1
            , cat2.category AS category2
        FROM purchased_categories cat1
        INNER JOIN purchased_categories cat2
            ON cat1.user_id = cat2.user_id
            AND cat1.category < cat2.category
    )
    , count_category_pairs AS (
        SELECT
            category1
            , category2
            , COUNT(*) AS customer_count
        FROM categories_pairs
        GROUP BY category1, category2
    )

SELECT *
FROM count_category_pairs
WHERE customer_count >= 3
ORDER BY customer_count DESC, category1, category2

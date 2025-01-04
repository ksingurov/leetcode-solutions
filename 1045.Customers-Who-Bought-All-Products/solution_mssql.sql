-- solution with lifehack
-- just count how many products and intrecept with distinct count in Customer
-- assumes there are no data quality issues
-- i.e. for example Customer table having not valid product_key's - not from Product table
-- TODO: check editorial if it solved the same, and then mark it as an issue

WITH
    product_count_per_customer AS (
        SELECT
            customer_id
            , COUNT(DISTINCT product_key) product_count
        FROM Customer
        GROUP BY customer_id
    )
    , product_count AS (
        SELECT COUNT(product_key) AS product_count
        FROM Product
    )

SELECT customer_id
FROM product_count_per_customer
INNER JOIN product_count
    ON product_count_per_customer.product_count = product_count.product_count

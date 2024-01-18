-- solution in which left table is UnitsSold and right table is Prices
-- to avoid missing products that have not been sold unique product_ids is created
-- then the resulting average_price is left joined to it

WITH
    sales_amount AS (
        SELECT
            p.product_id
            , p.price
            , us.units
            , CAST(p.price * us.units AS FLOAT) AS sales_amount
        FROM UnitsSold us
        LEFT JOIN Prices p
            ON p.product_id = us.product_id
            AND us.purchase_date BETWEEN p.start_date AND p.end_date
    )
    , average_price AS (
        SELECT
            product_id
            , ROUND(SUM(sales_amount) / SUM(units), 2) AS average_price
        FROM sales_amount
        GROUP BY product_id
    )
    , product_ids AS (
        SELECT DISTINCT
            product_id
        FROM Prices
    )

SELECT
    p.product_id
    , COALESCE(a.average_price, 0) AS average_price
FROM product_ids p
LEFT JOIN average_price a
ON p.product_id = a.product_id
-- Prices table is used as left table since it contains all products
-- i.e. UnitsSold may not contain all products, and if we used it as the left table,
-- we would not get the average price for products that have not been sold.
-- it should be noted that resulting sales_amount table may contain more rows 

WITH sales_amount AS (
    SELECT
        p.product_id
        , p.price
        , us.units
        , CAST(p.price * us.units AS FLOAT) AS sales_amount
    FROM Prices p
    LEFT JOIN UnitsSold us
        ON p.product_id = us.product_id
        AND us.purchase_date BETWEEN p.start_date AND p.end_date
)

SELECT
    product_id
    , COALESCE(ROUND(SUM(sales_amount) / SUM(units), 2), 0) AS average_price
FROM sales_amount
GROUP BY product_id
WITH
    Products_first_prices AS (
        SELECT DISTINCT
            product_id
            , 10 AS new_price
            , CAST('1900-01-01' AS DATE) AS change_date
        FROM Products
    )
    , Products_with_all_changes AS (
        SELECT * FROM Products
        UNION
        SELECT * FROM Products_first_prices
    )
    , Products_last_price AS (
        SELECT
            product_id
            , new_price
            , ROW_NUMBER() OVER (PARTITION BY product_id ORDER BY change_date DESC) AS row_n
        FROM Products_with_all_changes
        WHERE change_date <= '2019-08-16'
    )

SELECT
    product_id
    , new_price AS price
FROM Products_last_price
WHERE row_n = 1

WITH
    row_n_for_year AS (
        SELECT
            product_id
            , year
            , ROW_NUMBER() OVER (PARTITION BY product_id ORDER BY year) AS row_year
        FROM Sales
    )
    , first_year AS (
        SELECT
            product_id
            , year
        FROM row_n_for_year
        WHERE row_year = 1
    )
    , sales_in_first_year AS (
        SELECT
            s.product_id
            , s.year AS first_year
            , s.quantity
            , s.price
        FROM Sales s
        INNER JOIN first_year fy
            ON s.product_id = fy.product_id
            AND s.year = fy.year
    )

SELECT * FROM sales_in_first_year

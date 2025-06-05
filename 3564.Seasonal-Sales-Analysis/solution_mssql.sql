WITH
    sales_with_season_category AS(
        SELECT
            s.sale_date
            , s.quantity
            , s.quantity * s.price AS sale_revenue
            , CASE
                WHEN MONTH(sale_date) IN (12, 1, 2) THEN 'Winter'
                WHEN MONTH(sale_date) IN (3, 4, 5) THEN 'Spring'
                WHEN MONTH(sale_date) IN (6, 7, 8) THEN 'Summer'
                ELSE 'Fall'
            END AS season
            , p.category
        FROM sales s
        JOIN products p
            ON s.product_id  = p.product_id
    )
    , sales_group_by_season_category AS (
        SELECT
            season
            , category
            , SUM(quantity) AS total_quantity
            , SUM(sale_revenue) AS total_revenue
        FROM sales_with_season_category
        GROUP BY season, category
    )
    , row_n AS (
        SELECT
            season
            , category
            , total_quantity
            , total_revenue
            , ROW_NUMBER() OVER (PARTITION BY season ORDER BY total_quantity DESC, total_revenue DESC) AS row_n
        FROM sales_group_by_season_category
    )

SELECT
    season
    , category
    , total_quantity
    , total_revenue
FROM row_n
WHERE row_n = 1
ORDER BY season

WITH 
    amount_per_day AS (
        SELECT
            visited_on
            , CAST(SUM(amount) AS FLOAT) AS amount
        FROM Customer
        GROUP BY visited_on
    )
    , running_sum AS (
        SELECT
            visited_on
            , SUM(amount) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS amount
            , COUNT(*) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS days_count
        FROM amount_per_day
    )
    , running_average AS (
        SELECT
            visited_on
            , amount
            , ROUND(amount / 7, 2) AS average_amount
        FROM running_sum
        WHERE days_count = 7
    )

SELECT *
FROM running_average
ORDER BY visited_on

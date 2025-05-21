-- first solution
-- all three aggregates for SUM, AVG, COUNT are calculated
-- apparetly, the solution is not optimal since it calculates avg which could be calculated as SUM / COUNTq

WITH 
    amount_per_day AS (
        SELECT
            visited_on
            , CAST(SUM(amount) AS FLOAT) AS amount
        FROM Customer
        GROUP BY visited_on
    )
    , aggregates AS (
        SELECT
            visited_on
            , SUM(amount) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS amount
            , AVG(amount) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS average_amount
            , COUNT(*) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS days_count
        FROM amount_per_day
    )

SELECT
    visited_on
    , amount
    , ROUND(average_amount, 2) AS average_amount
FROM aggregates
WHERE days_count = 7
ORDER BY visited_on

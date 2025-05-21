-- second solution
-- AVG could be calculated as a SUM / COUNT and making the query more efficient

-- apparently, the it is not necessary to calculate the aggregates for the first 6 days
-- which could make the query even more efficient
-- is it possible to skip the first 6 days? - no

-- important note / limitations of the solution
-- also ROWS BETWEEN is used since it is said "here will be at least one customer every day"
-- however, it is not guaranteed that there are customer every day in reality
-- so it is better to use RANGE BETWEEN
-- also some dates could be missing in the data, but moving average should be still calculated for those dates
-- so, we need to create a proxy table with all dates in the range between min and max dates
-- and join aggretated sums per day to that table before calculating moving average

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

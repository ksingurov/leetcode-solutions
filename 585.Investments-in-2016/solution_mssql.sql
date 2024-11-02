WITH
    count_same_tiv_2015 AS (
        SELECT
            tiv_2016
            , lat
            , lon
            , COUNT(*) OVER (PARTITION BY tiv_2015) AS count_same_tiv_2015
        FROM Insurance
    )
    , not_the_same_city AS (
        SELECT
            lat
            , lon
        FROM Insurance
        GROUP BY lat, lon
        HAVING COUNT(*) < 2
    )
    , policyholders_satidfying_conditions AS (
        SELECT
            tiv_2016
        FROM count_same_tiv_2015
        INNER JOIN not_the_same_city
            ON count_same_tiv_2015.lat = not_the_same_city.lat
            AND count_same_tiv_2015.lon = not_the_same_city.lon
    )

SELECT SUM(tiv_2016) AS tiv_2016
FROM policyholders_satidfying_conditions

-- comments:
--  maybe CROSS JOIN is not the most elegant way to do this, but it works
--  also SELECT with VALUES cpould be used, but it would be less readable
--  when rounding the fraction, CAST is needed to avoid integer division
--  otherwise, the result would be rounded to 0.0


WITH
    distinct_users AS (
        SELECT
            COUNT(DISTINCT player_id) AS distinct_users
        FROM Activity
    )
    , prev_event_date AS (
        SELECT
            player_id
            , DATEADD(DAY, -1, event_date) AS event_date_minus_day
            , LAG(event_date) OVER (PARTITION BY player_id ORDER BY event_date) AS prev_event_date
        FROM Activity
    )
    , users_with_consequtive_logins AS (
        SELECT
            COUNT(DISTINCT player_id) AS users_with_consequtive_logins
        FROM prev_event_date
        WHERE event_date_minus_day = prev_event_date
    )

SELECT
    ROUND(CAST(users_with_consequtive_logins AS FLOAT) / distinct_users, 2) AS fraction
FROM users_with_consequtive_logins
CROSS JOIN distinct_users

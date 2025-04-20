-- commenets:
-- interesting problem to solve compared to the other Medium ones
-- there are multiple ways to perfrom pivoting in SQL
-- here I used the PIVOT function
-- others ususlly use SUM with CASE WHEN or JOIN
-- this could be discussed in the comments
-- that there is more elegant and efficient way to do this

WITH
    previous_activity AS (
        SELECT
            user_id
            , activity_type
            , LAG(activity_type) OVER (PARTITION BY user_id ORDER BY activity_date) AS previous_activity
        FROM UserActivity
    )
    , converted_users AS (
        SELECT
            user_id
        FROM previous_activity
        WHERE activity_type = 'paid' AND previous_activity = 'free_trial'
    )
    , UserActivity_for_converted_users AS (
        SELECT
            act.user_id
            , act.activity_type
            , AVG(CAST(activity_duration AS FLOAT)) AS avg_activity_duration
        FROM UserActivity act
        INNER JOIN converted_users conv ON act.user_id = conv.user_id
        WHERE act.activity_type IN ('free_trial', 'paid')
        GROUP BY act.user_id, act.activity_type
    )

SELECT
    user_id
    , ROUND(free_trial, 2) AS trial_avg_duration
    , ROUND(paid, 2) AS paid_avg_duration
FROM UserActivity_for_converted_users
PIVOT (
    MAX(avg_activity_duration)
    FOR activity_type IN ([free_trial], [paid])
) AS p

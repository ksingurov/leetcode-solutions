-- solutuon with EXISTS to filter out banned users
WITH
    unbanned_users AS (
        SELECT users_id
        FROM Users
        WHERE banned = 'No' AND role IN ('client', 'driver')
    )
    , trips_with_unbanned_users AS (
        SELECT
            tr.request_at
            , CASE
                WHEN tr.status IN ('cancelled_by_driver', 'cancelled_by_client') THEN 1
                ELSE 0
            END AS cancelled
        FROM Trips tr
        WHERE EXISTS (
            SELECT 1 FROM unbanned_users WHERE tr.client_id = users_id
        )
        AND EXISTS (
            SELECT 1 FROM unbanned_users WHERE tr.driver_id = users_id
        )
    )
    , trips_between_dates AS (
        SELECT
            request_at
            , COUNT(*) AS trips_per_day
            , SUM(cancelled) AS cancelled_trips_per_day
        FROM trips_with_unbanned_users
        WHERE request_at BETWEEN '2013-10-01' AND '2013-10-03'
        GROUP BY request_at
    )

SELECT
    request_at AS [Day]
    , ROUND( CAST(cancelled_trips_per_day AS FLOAT) / trips_per_day, 2) AS [Cancellation Rate]
FROM trips_between_dates

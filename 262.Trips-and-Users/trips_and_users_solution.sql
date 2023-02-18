WITH
    drivers AS (
        SELECT * FROM Users WHERE role = 'driver'
    )
    ,clients AS (
        SELECT * FROM Users WHERE role = 'client'
    )
    ,trips_with_unbanned_users AS (
        SELECT
            tr.request_at
            ,CASE
                WHEN tr.status IN ('cancelled_by_driver', 'cancelled_by_client') THEN 1
                ELSE 0
            END AS cancelled 
        FROM Trips tr
        LEFT JOIN drivers dr ON tr.driver_id = dr.users_id
        LEFT JOIN clients cl ON tr.client_id = cl.users_id
        WHERE dr.banned = 'No' AND cl.banned = 'No'
    )
    ,count_trips_between_dates AS (
        SELECT
            request_at
            ,COUNT(*) AS total
            ,SUM(cancelled) AS total_cancelled
        FROM trips_with_unbanned_users
        WHERE request_at BETWEEN "2013-10-01" AND "2013-10-03"
        GROUP BY request_at
    )

SELECT
    request_at AS Day
    ,ROUND(total_cancelled / total, 2) AS "Cancellation Rate"
FROM count_trips_between_dates
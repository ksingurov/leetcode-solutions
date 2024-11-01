-- comments:
-- condition "managerId IS NOT NULL" is added to avoid counting employees without a manager
-- however, test table is not designed to test this condition, and the result is not affected by this condition

WITH
count_direct_reports AS (
    SELECT
        managerId
        , COUNT(*) AS count_direct_reports
    FROM Employee
    WHERE managerId IS NOT NULL
    GROUP BY managerId
)
, managers_with_at_least_5_direct_reports AS (
    SELECT
        e.name
    FROM count_direct_reports c
    LEFT JOIN Employee e ON c.managerId = e.id
    WHERE c.count_direct_reports >=5
)

SELECT * FROM managers_with_at_least_5_direct_reports
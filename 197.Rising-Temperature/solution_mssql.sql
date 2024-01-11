WITH previous_temperature AS (
    SELECT
        id
        , temperature
        , LAG(temperature) OVER (ORDER BY recordDate) AS previous_temperature
    FROM Weather
)

SELECT id
FROM previous_temperature
WHERE temperature > previous_temperature

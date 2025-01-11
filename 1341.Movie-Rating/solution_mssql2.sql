-- solution with window functions
-- check peformance with

WITH UserRanks AS (
    SELECT u.name AS results,
           RANK() OVER (ORDER BY COUNT(*) DESC, u.name) AS rank
    FROM MovieRating r
    JOIN Users u ON r.user_id = u.user_id
    GROUP BY r.user_id, u.name
),
MovieRanks AS (
    SELECT m.title AS results,
           RANK() OVER (ORDER BY AVG(r.rating) DESC, m.title) AS rank
    FROM MovieRating r
    JOIN Movies m ON r.movie_id = m.movie_id
    WHERE r.created_at BETWEEN '2020-02-01' AND '2020-02-29'
    GROUP BY r.movie_id, m.title
)

SELECT results FROM UserRanks WHERE rank = 1
UNION
SELECT results FROM MovieRanks WHERE rank = 1;

-- comments:
-- Problem description is a bit ambiguous in the 2nd part:
-- Find the movie name with the highest average rating in February 2020
-- "in February 2020" could mean:
-- 1. The average rating of the movie in February 2020
-- 2. The average rating of the movie as of February 2020, i.e. the average rating of the movie before March 2020
-- Based on the test cases, it seems that the second interpretation is correct.

WITH
movies_rated_per_user AS (
    SELECT
        user_id
        , COUNT(*) AS movies_rated
    FROM MovieRating
    GROUP BY user_id
)
, user_who_rated_the_most AS (
    SELECT TOP 1
        u.name AS results
    FROM movies_rated_per_user m
    LEFT JOIN Users u ON m.user_id = u.user_id
    ORDER BY m.movies_rated DESC, u.name
)
, average_movie_ratings AS (
    SELECT
        movie_id
        , AVG(rating) AS average_movie_rating
    FROM MovieRating
    WHERE created_at < '2020-03-01'
    GROUP BY movie_id
)
, best_movie AS (
    SELECT TOP 1
        m.title AS results
    FROM average_movie_ratings a
    LEFT JOIN Movies m ON a.movie_id = m.movie_id
    ORDER BY average_movie_rating DESC, m.title
)

SELECT * FROM user_who_rated_the_most
UNION
SELECT * FROM best_movie

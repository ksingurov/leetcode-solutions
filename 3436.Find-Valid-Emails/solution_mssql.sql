WITH
    string_info AS (
        SELECT
            *
            , LEN(email) - LEN(REPLACE(email, '@', '')) AS at_count
            , CHARINDEX('@', email) AS at_index
            , CHARINDEX('.com', email) AS com_index
        FROM Users
    )
    , before_after_at AS (
        SELECT
            *
            , IIF(at_count = 1 AND com_index <> 0, SUBSTRING(email, 1, at_index - 1), NULL) AS before_at
            , IIF(at_count = 1 AND com_index <> 0, SUBSTRING(email, at_index + 1, com_index - at_index - 1), NULL) AS after_at
        FROM string_info
    )

SELECT
    user_id
    , email
FROM before_after_at
WHERE before_at NOT LIKE '%[^a-zA-Z0-9_]%'
    AND after_at NOT LIKE '%[^a-zA-Z]%'
ORDER BY user_id

WITH
    domain_start_index AS (
        SELECT
            *
            , CHARINDEX('@leetcode.com', mail) AS domain_start_index
        FROM Users
    )
    , prefix_name AS (
        SELECT
            *
            , IIF(domain_start_index > 0, SUBSTRING(mail, 1, domain_start_index - 1), NULL) AS prefix_name
        FROM domain_start_index
    )
    , valid_prefix_name AS (
        SELECT
            *
            , IIF(prefix_name LIKE '[a-zA-Z]%', 1, 0) AS prefix_name_starts_with_letter
            , IIF(prefix_name NOT LIKE '%[^a-zA-Z0-9_.-]%', 1, 0) AS prefix_name_valid_symbols
        FROM prefix_name
    )

SELECT
    user_id
    , name
    , mail
FROM valid_prefix_name
WHERE domain_start_index > 0
    AND prefix_name_starts_with_letter = 1
    AND prefix_name_valid_symbols = 1

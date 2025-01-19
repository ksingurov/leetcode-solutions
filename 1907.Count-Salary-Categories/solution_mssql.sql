WITH
    salary_categories AS (
        SELECT *
        FROM (VALUES ('Low Salary'), ('Average Salary'), ('High Salary')) AS v(category)
    )
    , income_categories AS (
        SELECT
            *
            , CASE
                WHEN income < 20000 THEN 'Low Salary'
                WHEN income > 50000 THEN 'High Salary'
                ELSE 'Average Salary'
            END AS category
        FROM Accounts
    )
    , accounts_count_per_category_preliminary AS (
        SELECT
            category
            , COUNT(*) AS accounts_count_preliminary
        FROM income_categories
        GROUP BY category
    ), accounts_count_per_category AS (
        SELECT
            cat.category
            , COALESCE(pre.accounts_count_preliminary, 0) AS accounts_count
        FROM salary_categories cat
        LEFT JOIN accounts_count_per_category_preliminary pre
            ON cat.category = pre.category
    )

SELECT * FROM accounts_count_per_category

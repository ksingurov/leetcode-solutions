WITH
    space_positions AS (
        -- Anchor: find first occurrence per content_id
        SELECT
            content_id
            , content_text
            , CHARINDEX(' ', content_text) AS position
            , 'space' AS separator_type
        FROM user_content
        WHERE CHARINDEX(' ', content_text) > 0

        UNION ALL

        -- Recursive: find next occurrence starting after previous position
        SELECT
            content_id
            , content_text
            , CHARINDEX(' ', content_text, position + 1) AS position
            , 'space' AS separator_type
        FROM Space_positions
        WHERE CHARINDEX(' ', content_text, position + 1) > 0
    )
    , hyphen_positions AS (
        -- Anchor: find first occurrence per content_id
        SELECT
            content_id
            , content_text
            , CHARINDEX('-', content_text) AS position
            , 'hyphen' AS separator_type
        FROM user_content
        WHERE CHARINDEX('-', content_text) > 0

        UNION ALL

        -- Recursive: find next occurrence starting after previous position
        SELECT
            content_id
            , content_text
            , CHARINDEX('-', content_text, position + 1) AS position
            , 'hyphen' AS separator_type
        FROM Space_positions
        WHERE CHARINDEX('-', content_text, position + 1) > 0
    )
    , first_letter_positions AS (
        SELECT
            content_id
            , content_text
            , position + 1 AS position
            , separator_type
        FROM space_positions
        -- OPTION (MAXRECURSION 0);

        UNION

        SELECT
            content_id
            , content_text
            , position + 1 AS position
            , separator_type
        FROM hyphen_positions

        UNION

        SELECT
            content_id
            , content_text
            , 1 AS position
            , NULL AS separator_type
        FROM user_content
        -- OPTION (MAXRECURSION 0)
    )
    , first_letter_positions_order AS (
        SELECT
            content_id
            , LOWER(content_text) AS content_text
            , position
            , ROW_NUMBER() OVER (PARTITION BY content_id ORDER BY position) AS position_order
            , separator_type            
        FROM first_letter_positions
    )
    -- Final recursive CTE
    , converted_text AS (
        -- Anchor
        SELECT
            content_id
            , content_text AS original_text
            , STUFF(
                content_text, 
                position,
                1,
                UPPER(SUBSTRING(content_text, position, 1))
            ) AS converted_text
            , position_order
        FROM first_letter_positions_order
        WHERE position_order = 1      
        UNION ALL
        -- Recursive
        SELECT
            converted.content_id
            , converted.original_text
            , STUFF(
                converted.converted_text, 
                original.position,
                1,
                UPPER(SUBSTRING(converted.converted_text, original.position, 1))
            ) AS converted_text
            , original.position_order
        FROM converted_text converted
        INNER JOIN first_letter_positions_order original
            ON converted.content_id = original.content_id
                AND converted.position_order + 1 = original.position_order
    )
    , converted_text_with_row_n AS (
        SELECT
            content_id
            , original_text
            , converted_text
            , ROW_NUMBER() OVER (PARTITION BY content_id ORDER BY position_order DESC) AS row_n
        FROM converted_text       
    )

-- SELECT * FROM converted_text
-- ORDER BY content_id, position_order


-- SELECT
--     *
--     , ROW_NUMBER() OVER (PARTITION BY content_id ORDER BY position_order DESC) AS row_n
-- FROM converted_text

SELECT
    content_id
    , original_text
    , converted_text
FROM converted_text_with_row_n
WHERE row_n = 1

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

SELECT
    content_id
    , content_text
    , position
    , separator_type
FROM space_positions

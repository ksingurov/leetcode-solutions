SELECT
    content_id
    , TRIM(value) AS word
FROM user_content
CROSS APPLY STRING_SPLIT(content_text, ' ')

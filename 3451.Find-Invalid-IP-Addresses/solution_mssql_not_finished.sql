WITH
    octet_1_end AS (
        SELECT
            *
            , LEN(ip) AS ip_len
            , CHARINDEX('.', ip) AS octet_1_end
        FROM logs
    )
    , octet_1 AS (
        SELECT
            *
            , SUBSTRING(ip, 1, octet_1_end - 1) AS octet_1
            , SUBSTRING(ip, octet_1_end + 1, ip_len) AS ip_rest
        FROM octet_1_end
    )
    , octet_2_end AS (
        SELECT
            *
            , CHARINDEX('.', ip_rest) AS octet_2_end
            -- , LEN(ip_rest) AS ip_len
        FROM octet_1
    )
    -- , second_octet AS (
    --     SELECT
    --         *
    --         , SUBSTRING(ip_rest, first_octet_end, second_octet_end - 1) AS second_octet
    --         -- , SUBSTRING(ip_rest, second_octet_end + 1, ip_len) AS ip_rest
    --     FROM second_octet_end
    -- )
    

SELECT * FROM octet_2_end
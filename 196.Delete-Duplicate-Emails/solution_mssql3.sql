-- with INDEX
-- doesnt pass in leetcode
-- [42S11] [Microsoft][ODBC Driver 17 for SQL Server][SQL Server]The operation failed because an index or statistics with name 'IX_Person_Email_Id' already exists on table 'Person'. (1913) (SQLExecDirectW)

CREATE NONCLUSTERED INDEX IX_Person_Email_Id
ON Person(email, id);

WITH row_n AS (
    SELECT
        id
        , ROW_NUMBER() OVER (PARTITION BY email ORDER BY id) AS row_n
    FROM Person
)

DELETE FROM Person
WHERE NOT EXISTS (
    SELECT 1 FROM row_n r WHERE r.row_n = 1 AND r.id = Person.id
)

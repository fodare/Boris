USE master;
GO

CREATE DATABASE Boris;
GO

USE Boris;
GO

CREATE SCHEMA UserSchema;
GO

CREATE TABLE UserSchema.Users
(
    id INT IDENTITY(1,1),
    Username VARCHAR(50) NOT NULL,
    Password VARCHAR(50) NOT NULL,
    CreateDate DATE,
    LastUpdates DATE
);
GO

CREATE CLUSTERED INDEX cix_Users_id
    ON UserSchema.Users (id);
GO

CREATE OR ALTER PROCEDURE UserSchema.spUser_Get
    /* EXEC UserSchema.spUser_Get @userId = 1 */
    /* EXEC UserSchema.spUser_Get @userName = 'jane' */
    @userId INT = NULL,
    @userName VARCHAR(50) = NULL
AS
BEGIN
    SELECT *
    FROM UserSchema.Users AS Users
    WHERE Users.[id] = ISNULL(@userId, id) AND Users.Username = ISNULL(@userName, Username)
END
GO

CREATE OR ALTER PROCEDURE UserSchema.spUser_Add
    /* EXEC UserSchema.spUser_Add 
    @userName = 'Jane2', 
    @password = 'janedoewwewe123', 
    @createDate = '2023-12-30', 
    @lastUpdates = '2023-12-30'
    */
    @userName VARCHAR(50),
    @password NVARCHAR(max),
    @createDate DATE,
    @lastUpdates DATE
AS
BEGIN
    IF NOT EXISTS (SELECT *
    FROM UserSchema.Users AS Users
    WHERE Users.Username = @userName)
    BEGIN
        INSERT INTO UserSchema.Users
            (
            [Username],
            [Password],
            [CreateDate],
            [LastUpdates]
            )
        OUTPUT
        INSERTED.Username
        VALUES(@userName, @password, @createDate, @lastUpdates)
    END
    ELSE
        THROW 52000,
        'Username exists. Please provide another username.',1;
END
GO


-- CREATE TABLE FinanceRecordSchema.UserRecord
-- (
--     UserId INT IDENTITY(1,1),
--     UserName VARCHAR(50),
--     UserPassword NVARCHAR(max),
--     IsAdmin BIT,
--     CreatedDate DATE,
--     UpdatedDate DATE
-- );
-- GO

-- CREATE CLUSTERED INDEX cix_UserRecord_UserId
--     ON FinanceRecordSchema.UserRecord(UserId);
-- GO

-- CREATE OR ALTER PROCEDURE FinanceRecordSchema.spRecord_Add
--     /* EXEC FinanceRecordSchema.spRecord_Add
--         @amount = 20.00, @recordType = 'Credit',
--         @recordTag = 'Savings', @recordNote = 'test',
--         @recordDate = '2023-12-31', @recordUpdateDate='2023-12-31'
--     */
--     @userId INT = 0,
--     @amount DECIMAL(18, 4),
--     @recordType VARCHAR(50),
--     @recordTag VARCHAR(50),
--     @recordNote VARCHAR(255),
--     @recordDate DATE,
--     @recordUpdateDate DATE
-- AS
-- BEGIN
--     INSERT INTO FinanceRecordSchema.Records
--         (
--         [UserId],[Amount],[RecordType],[RecordTag],
--         [RecordNote],[RecordDate],[RecordUpdateDate]
--         )
--     VALUES
--         (ISNULL(@userId, 0), @amount, @recordType, @recordTag, @recordNote, @recordDate, @recordUpdateDate)
-- END
-- GO

-- CREATE OR ALTER PROCEDURE FinanceRecordSchema.spRecord_Get
--     /* 
--     EXEC FinanceRecordSchema.spRecord_Get @recordId=1
--     EXEC FinanceRecordSchema.spRecord_Get @userId = 8
--     EXEC FinanceRecordSchema.spRecord_Get @startDate = '2024-03-01',
--         @endDate = '2024-05-28'
--     */
--     @recordId INT = null,
--     @userId INT = null,
--     @startDate DATE = null,
--     @endDate DATE =  NULL
-- AS
-- BEGIN
--     IF @startDate is NULL
--     BEGIN
--         SELECT TOP(10)
--             *
--         FROM FinanceRecordSchema.Records WITH(NOLOCK)
--         WHERE RecordId = ISNULL(@recordId , RecordId)
--             AND UserId = ISNULL(@userId, UserId)
--             AND RecordDate >= ISNULL(@startDate, RecordDate)
--             AND RecordUpdateDate <= ISNULL(@endDate, RecordUpdateDate)
--         ORDER By RecordDate DESC
--     END
--     ELSE
--         SELECT *
--     FROM FinanceRecordSchema.Records WITH(NOLOCK)
--     WHERE RecordId = ISNULL(@recordId , RecordId)
--         AND UserId = ISNULL(@userId, UserId)
--         AND RecordDate >= ISNULL(@startDate, RecordDate)
--         AND RecordUpdateDate <= ISNULL(@endDate, RecordUpdateDate)
--     ORDER By RecordDate DESC
-- END
-- GO

-- CREATE OR ALTER PROCEDURE FinanceRecordSchema.spRecord_Update
--     /* EXEC FinanceRecordSchema.spRecord_Update
--         @amount = 130, @recordType = 'Credit',
--         @recordTag = 'Eatingout', @recordNote = 'This is a test',
--         @RecordUpdateDate = '2024-01-01', @recordId = 5
--     */
--     @amount DECIMAL(18, 4),
--     @recordType VARCHAR(50),
--     @recordTag VARCHAR(50),
--     @recordNote VARCHAR(50),
--     @RecordUpdateDate DATETIME,
--     @recordId INT
-- AS
-- BEGIN
--     UPDATE FinanceRecordSchema.Records 
--         SET Amount = @amount, RecordType = @recordType,
--         RecordTag = @recordTag, RecordNote = @recordNote,
--         RecordUpdateDate = @RecordUpdateDate
--             WHERE RecordId = @recordId
-- END
-- GO
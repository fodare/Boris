USE master;
GO

CREATE DATABASE FinanceRecordDb;
GO

USE FinanceRecordDb;
GO

CREATE SCHEMA FinanceRecordSchema;
GO

CREATE TABLE FinanceRecordSchema.Records
(
    RecordId INT IDENTITY(1,1),
    UserId INT NOT NULL,
    Amount DECIMAL(18, 4),
    RecordType VARCHAR(50),
    RecordTag VARCHAR(50),
    RecordNote VARCHAR(255),
    RecordDate DATE,
    RecordUpdateDate DATE
);
GO

CREATE CLUSTERED INDEX cix_Records_RecordId
    ON FinanceRecordSchema.Records (RecordId);
GO

CREATE TABLE FinanceRecordSchema.UserRecord
(
    UserId INT IDENTITY(1,1),
    UserName VARCHAR(50),
    UserPassword NVARCHAR(max),
    IsAdmin BIT,
    CreatedDate DATE,
    UpdatedDate DATE
);
GO

CREATE CLUSTERED INDEX cix_UserRecord_UserId
    ON FinanceRecordSchema.UserRecord(UserId);
GO

CREATE OR ALTER PROCEDURE FinanceRecordSchema.spUser_Get
    /* EXEC FinanceRecordSchema.spUser_Get @userId = 6 */
    /* EXEC FinanceRecordSchema.spUser_Get @userName = 'jane' */
    @userId INT = NULL,
    @userName VARCHAR(50) = NULL
AS
BEGIN
    SELECT *
    FROM FinanceRecordSchema.UserRecord AS Users
    WHERE Users.[UserId] = ISNULL(@userId, UserId) AND Users.UserName = ISNULL(@userName, UserName)
END
GO

CREATE OR ALTER PROCEDURE FinanceRecordSchema.spUser_Add
    /* EXEC FinanceRecordSchema.spUser_Add 
        @userName = 'Jane', @userPassword = 'janedoewwewe123',
        @isAdmin = 1, @createDate = '2023-12-30', @updateDate = '2023-12-30'
    */
    @userName VARCHAR(50),
    @userPassword NVARCHAR(max),
    @isAdmin BIT = 0,
    @createDate DATE,
    @updateDate DATE
AS
BEGIN
    IF NOT EXISTS (SELECT *
    FROM FinanceRecordSchema.UserRecord AS Users
    WHERE Users.UserName = @userName)
    BEGIN
        INSERT INTO FinanceRecordSchema.UserRecord
            (
            [UserName],
            [UserPassword],
            [IsAdmin],
            [CreatedDate],
            [UpdatedDate]
            )
        VALUES(@userName, @userPassword, @isAdmin, @createDate, @updateDate)
    END
    ELSE
        THROW 52000,
        'Username exists. Please provide another username.',1;
END
GO


CREATE OR ALTER PROCEDURE FinanceRecordSchema.spRecord_Add
    /* EXEC FinanceRecordSchema.spRecord_Add
        @amount = 20.00, @recordType = 'Credit',
        @recordTag = 'Savings', @recordNote = 'test',
        @recordDate = '2023-12-31', @recordUpdateDate='2023-12-31'
    */
    @userId INT = 0,
    @amount DECIMAL(18, 4),
    @recordType VARCHAR(50),
    @recordTag VARCHAR(50),
    @recordNote VARCHAR(255),
    @recordDate DATE,
    @recordUpdateDate DATE
AS
BEGIN
    INSERT INTO FinanceRecordSchema.Records
        (
        [UserId],[Amount],[RecordType],[RecordTag],
        [RecordNote],[RecordDate],[RecordUpdateDate]
        )
    VALUES
        (ISNULL(@userId, 0), @amount, @recordType, @recordTag, @recordNote, @recordDate, @recordUpdateDate)
END
GO

CREATE OR ALTER PROCEDURE FinanceRecordSchema.spRecord_Get
    /* 
    EXEC FinanceRecordSchema.spRecord_Get @recordId=1
    EXEC FinanceRecordSchema.spRecord_Get @userId = 8
    EXEC FinanceRecordSchema.spRecord_Get @startDate = '2024-03-01',
        @endDate = '2024-05-28'
    */
    @recordId INT = null,
    @userId INT = null,
    @startDate DATE = null,
    @endDate DATE =  NULL
AS
BEGIN
    IF @startDate is NULL
    BEGIN
        SELECT TOP(10)
            *
        FROM FinanceRecordSchema.Records WITH(NOLOCK)
        WHERE RecordId = ISNULL(@recordId , RecordId)
            AND UserId = ISNULL(@userId, UserId)
            AND RecordDate >= ISNULL(@startDate, RecordDate)
            AND RecordUpdateDate <= ISNULL(@endDate, RecordUpdateDate)
        ORDER By RecordDate DESC
    END
    ELSE
        SELECT *
    FROM FinanceRecordSchema.Records WITH(NOLOCK)
    WHERE RecordId = ISNULL(@recordId , RecordId)
        AND UserId = ISNULL(@userId, UserId)
        AND RecordDate >= ISNULL(@startDate, RecordDate)
        AND RecordUpdateDate <= ISNULL(@endDate, RecordUpdateDate)
    ORDER By RecordDate DESC
END
GO

CREATE OR ALTER PROCEDURE FinanceRecordSchema.spRecord_Update
    /* EXEC FinanceRecordSchema.spRecord_Update
        @amount = 130, @recordType = 'Credit',
        @recordTag = 'Eatingout', @recordNote = 'This is a test',
        @RecordUpdateDate = '2024-01-01', @recordId = 5
    */
    @amount DECIMAL(18, 4),
    @recordType VARCHAR(50),
    @recordTag VARCHAR(50),
    @recordNote VARCHAR(50),
    @RecordUpdateDate DATETIME,
    @recordId INT
AS
BEGIN
    UPDATE FinanceRecordSchema.Records 
        SET Amount = @amount, RecordType = @recordType,
        RecordTag = @recordTag, RecordNote = @recordNote,
        RecordUpdateDate = @RecordUpdateDate
            WHERE RecordId = @recordId
END
GO
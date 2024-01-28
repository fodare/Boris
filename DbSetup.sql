USE master;
GO

CREATE DATABASE FinanceManagerDb;
GO

USE FinanceManagerDB;
GO

CREATE SCHEMA FinanceManagerSchema;
GO

CREATE TABLE FinanceManagerSchema.TransactionRecord
(
    TransactionId INT IDENTITY(1,1),
    UserId INT NOT NULL,
    Amount DECIMAL(18, 4),
    TransactionType VARCHAR(50),
    TransactionTag VARCHAR(50),
    Note VARCHAR(255),
    RecordDate DATETIME,
    UpdatedDate DATETIME
);
GO

CREATE CLUSTERED INDEX cix_TransactionRecord_TransactionId 
    ON FinanceManagerSchema.TransactionRecord (TransactionId);
GO

CREATE TABLE FinanceManagerSchema.UserRecord
(
    UserId INT IDENTITY(1,1),
    UserName VARCHAR(50),
    UserPassword NVARCHAR(max),
    IsAdmin BIT,
    CreatedDate Datetime,
    UpdatedDate Datetime
);
GO

CREATE CLUSTERED INDEX cix_UserRecord_UserId
    ON FinanceManagerSchema.UserRecord(UserId);
GO

CREATE OR ALTER PROCEDURE FinanceManagerSchema.spUser_Get
    /* EXEC FinanceManagerSchema.spUser_Get @userId = 2 */
    /* EXEC FinanceManagerSchema.spUser_Get @userName = 'string' */
    @userId INT = NULL,
    @userName VARCHAR(50) = NULL
AS
BEGIN
    SELECT *
    FROM FinanceManagerSchema.UserRecord AS Users
    WHERE Users.[UserId] = ISNULL(@userId, UserId) AND
        Users.UserName = ISNULL(@userName, UserName)
END
GO

CREATE OR ALTER PROCEDURE FinanceManagerSchema.spUser_Add
    /* EXEC FinanceManagerSchema.spUser_Add 
        @userName = 'Jane', @userPassword = 'janedoewwewe123',
        @isAdmin = 1, @createDate = '2023-12-30T17:31:30.368Z'
    */
    @userName VARCHAR(50),
    @userPassword NVARCHAR(max),
    @isAdmin BIT = 0,
    @createDate DATETIME
AS
BEGIN
    IF NOT EXISTS (SELECT *
    FROM FinanceManagerSchema.UserRecord AS Users
    WHERE Users.UserName = @userName)
    BEGIN
        INSERT INTO FinanceManagerSchema.UserRecord
            (
            [UserName],
            [UserPassword],
            [IsAdmin],
            [CreatedDate]
            )
        VALUES(@userName, @userPassword, @isAdmin, @createDate)
    END
    ELSE
        THROW 52000,
        'Username exists. Please provide another username.',1;
END
GO

CREATE OR ALTER PROCEDURE FinanceManagerSchema.spTransaction_Add
    /* EXEC FinanceManagerSchema.spTransaction_Add
        @amount = 20.00, @transactionType = 'Credit',
        @transactionTag = 'Savings', @note = 'test',
        @recordDate = '2023-12-31 15:43:49.000'
    */
    @userId INT = 0,
    @amount DECIMAL(18, 4),
    @transactionType VARCHAR(50),
    @transactionTag VARCHAR(50),
    @note VARCHAR(255),
    @recordDate Datetime
AS
BEGIN
    INSERT INTO FinanceManagerSchema.TransactionRecord
        (
        [UserId],[Amount],[TransactionType],[TransactionTag],
        [Note],[RecordDate]
        )
    VALUES
        (ISNULL(@userId, 0), @amount, @transactionType, @transactionTag, @note, @recordDate)
END
GO

CREATE OR ALTER PROCEDURE FinanceManagerSchema.spTransaction_Get
    /* EXEC FinanceManagerSchema.spTransaction_Get
        @transactionId = 1, @userId = 8
    */
    @transactionId INT = null,
    @userId INT = null
AS
BEGIN
    SELECT *
    FROM FinanceManagerSchema.TransactionRecord WITH(NOLOCK)
    WHERE TransactionId = ISNULL(@transactionId , TransactionId)
        AND UserId = ISNULL(@userId, UserId)
END
GO

CREATE OR ALTER PROCEDURE FinanceManagerSchema.spTransaction_Update
    /* EXEC FinanceManagerSchema.spTransaction_Update
        @amount = 130, @transactionType = 'Credit',
        @tranactionTag = 'Eatingout', @note = 'This is a test',
        @updateDate = '2024-01-01 20:36:31.000', @transactionId = 5
    */
    @amount INT,
    @transactionType VARCHAR(50),
    @tranactionTag VARCHAR(50),
    @note VARCHAR(50),
    @updateDate DATETIME,
    @transactionId INT
AS
BEGIN
    UPDATE FinanceManagerSchema.TransactionRecord 
        SET Amount = @amount, TransactionType = @transactionType,
        TransactionTag = @tranactionTag, Note = @note,
        UpdatedDate = @updateDate
            WHERE TransactionId = @transactionId
END
GO

Create OR ALTER PROCEDURE FinanceManagerSchema.spTransaction_Summary
    /* EXEC FinanceManagerSchema.spTransaction_Summary
    @startDate = '2024-01-01',
    @endDate = '2024-01-24'
  */
    @startDate DATETIME = null,
    @endDate DATETIME = null
AS
BEGIN
    SELECT
        TransactionTag,
        SUM(Amount) as Amount_Sum,
        COUNT(TransactionTag) as Event_count
    FROM FinanceManagerSchema.TransactionRecord
    WHERE RecordDate >= ISNULL(@startDate, RecordDate) AND RecordDate <= ISNULL(@endDate, RecordDate)
    GROUP BY TransactionTag
END
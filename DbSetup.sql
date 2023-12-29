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
    SpaceId INT NOT NULL,
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
    /* EXEC FinanceManagerSchema.spUser_Get @userId = 1  */
    @userId INT
AS
BEGIN
    SELECT *
    FROM FinanceManagerSchema.UserRecord AS Users
    WHERE Users.[UserId] = @userId;
END
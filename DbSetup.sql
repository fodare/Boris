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
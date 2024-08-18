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
    /* EXEC UserSchema.spUser_Get @userName = '' */
    @userId INT = NULL,
    @userName VARCHAR(50) = NULL
AS
BEGIN
    SELECT *
    FROM UserSchema.Users AS Users WITH (NOLOCK)
    WHERE Users.[id] = ISNULL(@userId, id) AND Users.Username = ISNULL(@userName, Username)
END
GO

CREATE OR ALTER PROCEDURE UserSchema.spUser_Add
    /* EXEC UserSchema.spUser_Add 
    @userName = '', 
    @password = '', 
    @createDate = '', 
    @lastUpdates = ''
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

CREATE SCHEMA PasswordSchema;
GO


CREATE TABLE PasswordSchema.Passwords
(
    id INT IDENTITY(1,1),
    Account VARCHAR(50) NOT NULL,
    Username VARCHAR(90) NOT NULL,
    Password NVARCHAR(max) NOT NULL,
    LoginLink NVARCHAR(max),
    Note NVARCHAR(max)
);
GO

CREATE CLUSTERED INDEX cix_Passwords_id
    ON PasswordSchema.Passwords(id);
GO

CREATE OR ALTER PROCEDURE PasswordSchema.spPasswords_Get
    /* 
        EXEC PasswordSchema.spPasswords_Get @id=1
        EXEC PasswordSchema.spPasswords_Get @account=''
    */
    @id int = null,
    @account VARCHAR(50) = null
AS
BEGIN
    SELECT *
    FROM PasswordSchema.Passwords AS Passwords WITH (NOLOCK)
    WHERE Passwords.[id] = ISNULL(@id, id) AND Passwords.Account = ISNULL(@account, Account)
END
GO

CREATE OR ALTER PROCEDURE PasswordSchema.spPasswords_Add
    /* 
        EXEC PasswordSchema.spPasswords_Add
        @account='', @username ='',
        @password='', @link='', @note=''
    */
    @account VARCHAR(50),
    @username VARCHAR(90),
    @password NVARCHAR(max),
    @link NVARCHAR(max),
    @note NVARCHAR(max)
AS
BEGIN
    IF NOT EXISTS (SELECT *
    FROM PasswordSchema.Passwords AS Passwords WITH (NOLOCK)
    WHERE Passwords.Account = @account)
    BEGIN
        INSERT INTO PasswordSchema.Passwords
            ([Account],[Username],[Password],[LoginLink],[Note])
        OUTPUT
        INSERTED.Account
        VALUES
            (ISNULL(@account, ' '), @username, @password, @link, @note)
    END
    ELSE
        THROW 52000,
        'Account already exists. Please try with another account',1;
END
GO

CREATE OR ALTER PROCEDURE PasswordSchema.spPasswords_Update
    /* 
        EXEC PasswordSchema.spPasswords_Update
        @id=0, @account = '', @username = '',
        @password = '', @link='', @note = ''
    */
    @id INT,
    @account VARCHAR(50),
    @username VARCHAR(90),
    @password NVARCHAR(max),
    @link NVARCHAR(max),
    @note NVARCHAR(max)
AS
BEGIN
    UPDATE PasswordSchema.Passwords SET 
        [Account] = @account, [Username] = @username,
        [Password] = @password, [LoginLink] = @link, [Note] = @note
        OUTPUT
    INSERTED.Account
    WHERE [id] = @id
END
GO

CREATE OR ALTER PROCEDURE PasswordSchema.spPasswords_Delete
    /* 
        EXEC PasswordSchema.spPasswords_Delete @id= 0
    */
    @id INT = NULL,
    @account VARCHAR(50) = NULL
AS
BEGIN
    DELETE FROM PasswordSchema.Passwords 
    OUTPUT DELETED.id
    WHERE Passwords.id = ISNULL(@id, id)
END
GO
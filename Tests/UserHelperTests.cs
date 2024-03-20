namespace Tests;

using backend.Helpers;
using System;
using System.Reflection;
using Xunit;

public class UserHelperTests
{
    private static readonly Random random = new();
    private static readonly UserHelper userHelper = new();

    public string RandomTestPasswordGenerator()
    {
        const string allowedChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
        return new string(Enumerable.Repeat(allowedChars, 10)
            .Select(s => s[random.Next(s.Length)]).ToArray());
    }

    [Fact]
    public void Password_Hash_Created()
    {
        // Arrange
        string testPassword = RandomTestPasswordGenerator();
        bool passwordHashed = false;

        // Act
        string hashedPassword = userHelper.CreatePasswordHash(testPassword);
        if (hashedPassword != null)
        {
            passwordHashed = true;
        }

        // Assert
        Assert.True(passwordHashed);
    }

    [Fact]
    public void Password_Hash_Verification_works()
    {
        // Arrange
        string testPassword = RandomTestPasswordGenerator();
        bool passwordMatch = false;

        // Act
        string hashedPassword = userHelper.CreatePasswordHash(testPassword);

        // Assert
        Assert.True(userHelper.VerifyPasswordHash(testPassword, hashedPassword));
    }
}
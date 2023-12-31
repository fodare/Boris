using System;
using Microsoft.AspNetCore.Identity;

namespace backend.Helpers
{
    public class UserHelper
    {
        public string createPasswordHash(string password)
        {
            var hashedPassword = new PasswordHasher<object?>().HashPassword(null, password);
            return hashedPassword;
        }
    }
}
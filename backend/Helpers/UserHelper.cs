using System;
using System.Diagnostics;
using Microsoft.AspNetCore.Identity;

namespace backend.Helpers
{
    public class UserHelper
    {
        public string CreatePasswordHash(string password)
        {
            var hashedPassword = new PasswordHasher<object?>().HashPassword(null, password);
            return hashedPassword;
        }

        public bool VerifyPasswordHash(string password, string hashedPassword)
        {
            var passwordVerificationResult = new PasswordHasher<object?>()
                .VerifyHashedPassword(null, hashedPassword, password);
            return passwordVerificationResult switch
            {
                PasswordVerificationResult.Failed => false,
                PasswordVerificationResult.Success => true,
                PasswordVerificationResult.SuccessRehashNeeded => true,
                _ => false,
            };
        }
    }
}
using backend.Models;
using Microsoft.AspNetCore.Identity;

namespace backend.Helpers
{
    public class UserHelper
    {
        public string CreatePasswordHash(string password)
        {
            var hashedPassword = new PasswordHasher<UserModel?>().HashPassword(null, password);
            return hashedPassword;
        }

        public bool VerifyPasswordHash(string password, string hashedPassword)
        {
            var passwordVerificationResult = new PasswordHasher<UserModel?>()
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
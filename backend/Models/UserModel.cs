using System;
using System.Text.Json.Serialization;

namespace backend.Models
{
    public class UserModel
    {
        public int UserId { get; set; }

        [JsonPropertyName("userName")]
        public required string UserName { get; set; }

        [JsonPropertyName("password")]
        public required string UserPassword { get; set; }

        public required bool IsAdmin { get; set; }

        public DateOnly CreatedDate { get; set; }

        public DateOnly UpdatedDate { get; set; }
    }
}
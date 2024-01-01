using System;
using System.Text.Json.Serialization;

namespace backend.Models
{
    public class UserModel
    {
        public int UserId { get; set; }

        [JsonPropertyName("userName")]
        public string UserName { get; set; } = "";

        [JsonPropertyName("password")]
        public string UserPassword { get; set; } = "";

        public bool IsAdmin { get; set; }

        public DateTime CreatedDate { get; set; }

        public DateTime UpdatedDate { get; set; }
    }
}
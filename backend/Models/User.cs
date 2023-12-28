using System;
using System.Text.Json.Serialization;

namespace backend.Models
{
    public class User
    {
        public int UserId { get; set; }

        [JsonPropertyName("userName")]
        public string UserName { get; set; } = "";

        [JsonPropertyName("password")]
        public string Password { get; set; } = "";

        [JsonPropertyName("userFullName")]
        public string userFullName { get; set; } = "";

        public bool IsAdmin { get; set; }

        public DateTime CreatedDate { get; set; }

        public DateTime UpdatedDate { get; set; }
    }
}
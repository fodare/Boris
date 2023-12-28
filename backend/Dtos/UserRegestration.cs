using System;
using System.Text.Json.Serialization;

namespace backend.Dtos
{
    public class UserRegestration
    {
        [JsonPropertyName("userName")]
        public string UserName { get; set; } = "";

        [JsonPropertyName("password")]
        public string Password { get; set; } = "";

        [JsonPropertyName("userFullName")]
        public string userFullName { get; set; } = "";
    }
}
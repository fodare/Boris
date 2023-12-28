using System;
using System.Text.Json.Serialization;

namespace backend.Dtos
{
    public class LoginDto
    {
        [JsonPropertyName("userName")]
        public string UserName { get; set; } = "";

        [JsonPropertyName("password")]
        public string Password { get; set; } = "";
    }
}
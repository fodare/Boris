using System;
using System.Text.Json.Serialization;
using backend.Models;
namespace backend.Dtos
{
    public class GetUserDto
    {
        public int UserId { get; set; }

        [JsonPropertyName("userName")]
        public string UserName { get; set; } = "";

        public bool IsAdmin { get; set; }

        public DateTime CreatedDate { get; set; }

        public DateTime UpdatedDate { get; set; }
    }
}
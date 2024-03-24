using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.Json.Serialization;
using System.Threading.Tasks;

namespace backend.Dtos
{
    public class GetUserDTO
    {
        [JsonPropertyName("id")]
        public int UserId { get; set; }

        [JsonPropertyName("userName")]
        public string UserName { get; set; } = "";

        [JsonPropertyName("isAdmin")]
        public bool IsAdmin { get; set; }

        [JsonPropertyName("created")]
        public DateTime CreatedDate { get; set; }

        [JsonPropertyName("lastUpdated")]
        public DateTime UpdatedDate { get; set; }
    }
}
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.Json.Serialization;
using System.Threading.Tasks;

namespace backend.Dtos
{
    public class NewUserDTO
    {
        [JsonPropertyName("userName")]
        public required string UserName { get; set; }

        [JsonPropertyName("password")]
        public required string UserPassword { get; set; }
    }
}
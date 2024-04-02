using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.Json.Serialization;
using System.Threading.Tasks;
using backend.Models;

namespace backend.Dtos
{
    public class UpdateRecordDTO
    {
        [JsonPropertyName("amount")]
        public required double Amount { get; set; }

        [JsonPropertyName("event")]
        public required Recordtype Recordtype { get; set; }

        [JsonPropertyName("tag")]
        public required string RecordTag { get; set; }

        [JsonPropertyName("note")]
        public required string RecordNote { get; set; }

    }
}
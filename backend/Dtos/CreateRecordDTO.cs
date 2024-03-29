using System.Text.Json.Serialization;
using backend.Models;

namespace backend.Dtos
{
    public class CreateRecordDTO
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
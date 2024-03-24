using System;
using System.Security;
using System.Text.Json.Serialization;

namespace backend.Models
{
    public class RecordModel
    {
        public int RecordId { get; set; }

        public int UserId { get; set; }

        [JsonPropertyName("amount")]
        public required double Amount { get; set; }

        [JsonPropertyName("recordType")]
        public required Recordtype Recordtype { get; set; }

        [JsonPropertyName("recordTag")]
        public required string RecordTag { get; set; }

        [JsonPropertyName("note")]
        public string? RecordNote { get; set; }

        public DateOnly RecordDate { get; set; }
        public DateOnly RecordUpdateDate { get; set; }
    }
}
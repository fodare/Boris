using System.Text.Json.Serialization;
using backend.Models;

namespace backend.Dtos
{
    public class GetRecordDTO
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

        [JsonPropertyName("total ")]
        public double Total { get; set; }

    }
}
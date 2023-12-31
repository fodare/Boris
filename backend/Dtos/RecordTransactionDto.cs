using System;
using System.Text.Json.Serialization;
using backend.Models;
namespace backend.Dtos
{
    public class RecordTransactionDto
    {
        [JsonPropertyName("spaceId")]
        public int SpaceId { get; set; }

        [JsonPropertyName("amount")]
        public double Amount { get; set; }

        [JsonPropertyName("type")]
        public Transactiontype Type { get; set; }

        [JsonPropertyName("tag")]
        public Recordtype Tag { get; set; }

        [JsonPropertyName("note")]
        public string Note { get; set; } = "";
    }
}
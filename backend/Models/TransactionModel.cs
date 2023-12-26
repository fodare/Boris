using System;
using System.Text.Json.Serialization;

namespace backend.Models
{
    public class TransactionModel
    {
        public int TransactionId { get; set; }

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

        [JsonPropertyName("recordDate")]
        public DateTime RecordDate { get; set; }

        [JsonPropertyName("lastUpdateDate")]
        public DateTime LastUpdatedDate { get; set; }
    }
}
using System;
using System.Text.Json.Serialization;

namespace backend.Models
{
    public class TransactionModel
    {
        public int TransactionId { get; set; }

        public int UserId { get; set; }

        [JsonPropertyName("amount")]
        public double Amount { get; set; }

        [JsonPropertyName("type")]
        public Transactiontype TransactionType { get; set; }

        [JsonPropertyName("tag")]
        public Recordtype TransactionTag { get; set; }

        [JsonPropertyName("note")]
        public string Note { get; set; } = "";

        [JsonPropertyName("recordDate")]
        public DateTime RecordDate { get; set; }

        [JsonPropertyName("lastUpdateDate")]
        public DateTime UpdatedDate { get; set; }
    }
}
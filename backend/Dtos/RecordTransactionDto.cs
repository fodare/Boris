using System;
using System.Text.Json.Serialization;
using backend.Models;
namespace backend.Dtos
{
    public class RecordTransactionDto
    {
        [JsonPropertyName("amount")]
        public double Amount { get; set; }

        [JsonPropertyName("type")]
        public Transactiontype TransactionType { get; set; }

        [JsonPropertyName("tag")]
        public Recordtype TransactionTag { get; set; }

        [JsonPropertyName("note")]
        public string Note { get; set; } = "";
    }
}
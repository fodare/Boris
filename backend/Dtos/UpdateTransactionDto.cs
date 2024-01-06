using System;
using System.Text.Json.Serialization;
using backend.Models;
namespace backend.Dtos
{
    public class UpdateTransactionDto
    {
        [JsonPropertyName("amount")]
        public double Amount { get; set; }

        [JsonPropertyName("transactionType")]
        public Transactiontype Type { get; set; }

        [JsonPropertyName("transactionTag")]
        public Recordtype Tag { get; set; }

        [JsonPropertyName("note")]
        public string Note { get; set; } = "";
    }
}
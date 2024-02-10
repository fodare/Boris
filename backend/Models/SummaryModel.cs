using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.Json.Serialization;
using System.Threading.Tasks;

namespace backend.Models
{
    public class SummaryModel
    {
        [JsonPropertyName("tag")]
        public Recordtype TransactionTag { get; set; }

        [JsonPropertyName("amount")]
        public double Amount_Sum { get; set; }

        [JsonPropertyName("count")]
        public int Event_Count { get; set; }

        [JsonPropertyName("creditSum")]
        public double Credit_Sum { get; set; }

        [JsonPropertyName("debitSum")]
        public double Debit_Sum { get; set; }
    }
}
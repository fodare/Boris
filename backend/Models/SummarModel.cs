using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.Json.Serialization;
using System.Threading.Tasks;

namespace backend.Models
{
    public class SummarModel
    {
        [JsonPropertyName("tag")]
        public Recordtype TransactionTag { get; set; }
        [JsonPropertyName("amount")]
        public double Amount { get; set; }
        public int Event_Count { get; set; }
    }
}
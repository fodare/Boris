using System.Text.Json.Serialization;
using backend.Models;
using Xunit;

namespace backend.Dtos
{
    public class GetRecordDTO
    {
        public IEnumerable<RecordModel>? Records { get; set; }
        public double CreditTotal { get; set; }
        public double DebitTotal { get; set; }
    }
}
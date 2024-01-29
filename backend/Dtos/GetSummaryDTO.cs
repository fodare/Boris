using System.Text.Json.Serialization;

namespace backend.Dtos
{
    public class GetSummaryDTO
    {
        [JsonPropertyName("startTime")]
        public DateOnly Starttime { get; set; }

        [JsonPropertyName("endtime")]
        public DateOnly Endtime { get; set; }
    }
}
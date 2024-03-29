using backend.Dtos;
using backend.Models;

namespace backend.Services
{
    public interface IRecordService
    {
        bool CreateRecord(CreateRecordDTO newRecord);

        RecordModel? GetRecordById(int id);

        IEnumerable<GetRecordDTO> GetRecords();

        bool UpdateRecord(int id, UpdateRecordDTO modifiedRecord);

        IEnumerable<GetRecordDTO> GetRecordsByDateRange(DateOnly startDate, DateOnly endDate);
    }
}
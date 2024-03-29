using backend.Dtos;
using backend.Models;

namespace backend.Services
{
    public interface IRecordService
    {
        bool CreateRecord(CreateRecordDTO newRecord);

        RecordModel? GetRecordById(int id);

        IEnumerable<RecordModel>? GetRecords();

        bool UpdateRecord(int id, UpdateRecordDTO modifiedRecord);

        IEnumerable<RecordModel>? GetRecordsByDateRange(DateTime startDate, DateTime endDate);
    }
}
using backend.Data;
using backend.Dtos;
using backend.Models;

namespace backend.Services
{
    public class RecordService : IRecordService
    {
        private readonly DataContextDapper _dapper;
        public RecordService()
        {
            _dapper = new DataContextDapper();
        }

        public bool CreateRecord(CreateRecordDTO newRecord)
        {
            throw new NotImplementedException();
        }

        public RecordModel? GetRecordById(int id)
        {
            throw new NotImplementedException();
        }

        public IEnumerable<GetRecordDTO> GetRecords()
        {
            throw new NotImplementedException();
        }

        public IEnumerable<GetRecordDTO> GetRecordsByDateRange(DateOnly startDate, DateOnly endDate)
        {
            throw new NotImplementedException();
        }

        public bool UpdateRecord(int id, UpdateRecordDTO modifiedRecord)
        {
            throw new NotImplementedException();
        }
    }
}
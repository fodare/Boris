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
            try
            {
                static string getServerTime() => DateTime.Now.ToString("yyyy-MM-dd");
                string sqlCommand = $@"EXEC FinanceRecordSchema.spRecord_Add 
                    @amount = {newRecord.Amount}, @recordType = '{newRecord.Recordtype}', @recordTag = '{newRecord.RecordTag}', @recordNote = '{newRecord.RecordNote}', @recordDate = '{getServerTime()}', @recordUpdateDate='{getServerTime()}'";
                bool userAdded = _dapper.ExcecuteSqlAdd(sqlCommand);
                if (!userAdded)
                {
                    Console.WriteLine("Error creating user. Please try again!");
                    return false;
                }
                return true;
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error creating user. Error {ex.Message}");
                return false;
            }
        }

        public RecordModel? GetRecordById(int id)
        {
            string sqlCommand = $@"EXEC FinanceRecordSchema.spRecord_Get @recordId={id}";
            try
            {
                var quriedRecord = _dapper.LoadDataSingle<RecordModel>(sqlCommand);
                if (quriedRecord.RecordId == id)
                {
                    return quriedRecord;
                }
                return null;
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error fetching record id {id}. {ex.Message}");
                return null;
            }
        }

        public IEnumerable<RecordModel>? GetRecords()
        {
            try
            {
                string sqlCommand = $@"EXEC FinanceRecordSchema.spRecord_Get";
                IEnumerable<RecordModel> recordList = _dapper.LoadData<RecordModel>(sqlCommand);
                return recordList;
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error fetching records. Error {ex.Message}");
                return null;
            }
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
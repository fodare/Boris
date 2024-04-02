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

        public IEnumerable<RecordModel>? GetRecordsByDateRange(string startDate, string endDate)
        {
            string sqlCommand = $@"EXEC FinanceRecordSchema.spRecord_Get @startDate = '{startDate}', @endDate = '{endDate}'";
            try
            {
                IEnumerable<RecordModel>? recorList = _dapper.LoadData<RecordModel>(sqlCommand);
                if (recorList is null)
                {
                    return null;
                }
                return recorList;
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error fetching records from {startDate} - {endDate}. {ex}");
                return null;
            }
        }

        public bool UpdateRecord(int id, UpdateRecordDTO modifiedRecord)
        {
            static string getServerTime() => DateTime.Now.ToString("yyyy-MM-dd");

            string sqlCommand = $@"EXEC FinanceRecordSchema.spRecord_Update @amount={modifiedRecord.Amount}, @recordType='{modifiedRecord.Recordtype}', @recordTag='{modifiedRecord.RecordTag}', @recordNote='{modifiedRecord.RecordNote}',@RecordUpdateDate='{getServerTime()}', @recordId={id}";

            string sqlCommandCheckRecord = $@"EXEC FinanceRecordSchema.spRecord_Get @recordId={id}";

            try
            {
                RecordModel queridRecord = _dapper.ExecuteSql<RecordModel>(sqlCommandCheckRecord);
                if (queridRecord.RecordId != id)
                {
                    return false;
                }
                bool recordUpdated = _dapper.ExcecuteSqlAdd(sqlCommand);
                return true;
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error updating record Id {id}. {ex.Message}");
                return false;
            }
        }
    }
}
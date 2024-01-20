using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection.Metadata;
using System.Threading.Tasks;
using backend.Data;
using backend.Dtos;
using backend.Models;

namespace backend.Services
{
    public class TransactionService : ITransactionService
    {
        private readonly DataContextDapper _dapper;
        public TransactionService()
        {
            _dapper = new DataContextDapper();
        }

        public IEnumerable<TransactionModel>? GetTransactions()
        {
            string sqlCommand = "EXEC FinanceManagerSchema.spTransaction_Get";
            try
            {
                IEnumerable<TransactionModel> transactionsList = _dapper.LoadData<TransactionModel>(sqlCommand);
                return transactionsList;
            }
            catch (Exception e)
            {
                Console.WriteLine($"Error fetching transaction list. {e.Message}");
                return null;
            }
        }

        public TransactionModel? GetTransaction(int transactionId)
        {
            try
            {
                string sqlCommand = $@"EXEC FinanceManagerSchema.spTransaction_Get
                @transactionId = {transactionId}";

                var qureidUser = _dapper.LoadDataSingle<TransactionModel>(sqlCommand);
                if (qureidUser.TransactionId > 0)
                {
                    return qureidUser;
                }
                else
                {
                    return null;
                }
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
                return null;
            }
        }

        public bool RecordTransaction(RecordTransactionDto newRecord)
        {
            try
            {
                string sqlCommand = @$"EXEC FinanceManagerSchema.spTransaction_Add
                @userId = 1, @amount = {newRecord.Amount}, @transactionType = '{newRecord.TransactionType}',
                @transactionTag = '{newRecord.TransactionTag}', @note = '{newRecord.Note}',
                @recordDate = '{DateTime.Now}'
                ";
                bool userAdded = _dapper.ExcecuteSqlAdd(sqlCommand);
                if (userAdded)
                {
                    return true;
                }
                else { return false; }
            }
            catch (Exception e)
            {
                Console.WriteLine(e);
                return false;
            }
        }

        public bool UpdateTransactionRecord(UpdateTransactionDto updatedRecord,
            int transactionId)
        {
            string sqlCommandUpdate = @$"EXEC FinanceManagerSchema.spTransaction_Update
            @amount = {updatedRecord.Amount}, @transactionType = '{updatedRecord.Type}', 
            @tranactionTag = '{updatedRecord.Tag}',  @note = '{updatedRecord.Note}', 
            @updateDate = '{DateTime.Now}',  @transactionId = {transactionId}";

            string sqlCommandCheckTransaction = $@"EXEC FinanceManagerSchema.spTransaction_Get
            @transactionId = {transactionId}";
            try
            {
                TransactionModel qureiedTransaction = _dapper
                    .ExecuteSql<TransactionModel>(sqlCommandCheckTransaction);
                if (qureiedTransaction.TransactionId == transactionId)
                {
                    bool transactionRecord = _dapper.ExcecuteSqlAdd(sqlCommandUpdate);
                    return true;
                }
                else
                {
                    return false;
                }
            }
            catch (Exception e)
            {
                Console.WriteLine($"Error updating transaction record. {e.Message}");
                return false;
            }

        }
    }
}
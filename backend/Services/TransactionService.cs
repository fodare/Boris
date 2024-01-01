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
        public Task<ResponseModel<bool>> DeleteTransactionRecord(int trasnactionId)
        {
            throw new NotImplementedException();
        }

        public Task<ResponseModel<TransactionModel>> GetTransaction(int transactionId)
        {
            throw new NotImplementedException();
        }

        public Task<ResponseModel<IEnumerable<TransactionModel>>> GetTransactions()
        {
            throw new NotImplementedException();
        }

        public async Task<bool> RecordTransaction(RecordTransactionDto newRecord)
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

        public Task<ResponseModel<bool>> UpdateTransactionRecord(UpdateTransactionDto updatedRecord)
        {
            throw new NotImplementedException();
        }
    }
}
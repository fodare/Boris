using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using backend.Dtos;
using backend.Models;

namespace backend.Services
{
    public class TransactionService : ITransactionService
    {
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

        public Task<ResponseModel<bool>> RecordTransaction(RecordTransactionDto newRecord)
        {
            throw new NotImplementedException();
        }

        public Task<ResponseModel<bool>> UpdateTransactionRecord(UpdateTransactionDto updatedRecord)
        {
            throw new NotImplementedException();
        }
    }
}
using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection.Metadata;
using System.Threading.Tasks;
using System.Transactions;
using backend.Dtos;
using backend.Models;

namespace backend.Services
{
    public interface ITransactionService
    {
        Task<IEnumerable<TransactionModel>> GetTransactions();

        Task<TransactionModel> GetTransaction(int transactionId);

        Task<bool> RecordTransaction(RecordTransactionDto newRecord);

        Task<bool> UpdateTransactionRecord(UpdateTransactionDto updatedRecord,
            int transactionId);
    }
}
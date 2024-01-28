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
        IEnumerable<TransactionModel>? GetTransactions();

        IEnumerable<SummaryModel>? GetSummary(GetSummaryDTO queryTime);

        TransactionModel? GetTransaction(int transactionId);

        bool RecordTransaction(RecordTransactionDto newRecord);

        bool UpdateTransactionRecord(UpdateTransactionDto updatedRecord, int transactionId);
    }
}
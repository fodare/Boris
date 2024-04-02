using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Reflection.Metadata;
using System.Threading.Tasks;
using backend.Controllers;
using backend.Models;

namespace backend.Helpers
{
    public class RecrodsHelper
    {
        public double CalculateCreditSum(IEnumerable<RecordModel> records)
        {
            double creditSum = 0;
            foreach (RecordModel record in records)
            {
                if (record.Recordtype == Recordtype.Credit)
                {
                    creditSum += record.Amount;
                }
            }
            return creditSum;
        }

        public double CalculateDebitSum(IEnumerable<RecordModel> records)
        {
            double debitSum = 0;
            foreach (RecordModel record in records)
            {
                if (record.Recordtype == Recordtype.Debit)
                {
                    debitSum += record.Amount;
                }
            }
            return debitSum;
        }
    }
}
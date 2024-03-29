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
        public double CalculateRecordsAmountSum(IEnumerable<RecordModel> records)
        {
            double amountSum = 0;
            foreach (RecordModel record in records)
            {
                amountSum += record.Amount;
            }
            return amountSum;
        }
    }
}
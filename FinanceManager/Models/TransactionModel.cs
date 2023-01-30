using Microsoft.EntityFrameworkCore.Metadata.Internal;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace FinanceManager.Models
{
    public class TransactionModel
    {

        public int Id { get; set; }

        [Column(TypeName = "decimal(18, 2)")]
        [DataType(DataType.Currency)]
        public decimal Amount { get; set; }

        [Display(Name = "Transacttion Date")]
        [DataType(DataType.Date)]
        public DateTime TransactionDate { get; set; }
        [Display(Name = "Transacttion Type")]
        public TransactionType TransactionType { get; set; }
        [Display(Name = "Transacttion Note")]
        public string TransctionNote { get; set; } = string.Empty;
        public TransactionForm TransactionForm { get; set; }

    }
    public enum TransactionType
    {
        EatingOut,
        Grocery,
        Fmaily,
        Freinds,
        Electic_Bill,
        Internet_Bill,
        Tv_Bill,
        Clothing,
        Sanitary,
        Emergency,
        Insurance,
        Personal_Development,
        Savings,
        Rent,
    }
    public enum TransactionForm
    {
        Credit,
        Debit
    }

}
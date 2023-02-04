using Microsoft.EntityFrameworkCore.Metadata.Internal;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace FinanceManager.Models
{
    public class Summation
    {
        public int Id { get; set; }

        [Column(TypeName = "decimal(18, 2)")]
        [DataType(DataType.Currency)]
        public decimal TotalSavngs { get; set; }

        [Column(TypeName = "decimal(18, 2)")]
        [DataType(DataType.Currency)]
        public decimal TotalSpending { get; set; }

        [Display(Name = "Last updated")]
        [DataType(DataType.Date)]
        public DateTime LastUpdateDate { get; set; }
    }
}

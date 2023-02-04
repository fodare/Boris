using FinanceManager.Models;
using Microsoft.EntityFrameworkCore;
using System.Transactions;

namespace FinanceManager.Data
{
    public class DataContext : DbContext
    {
        public DataContext(DbContextOptions<DataContext> options) : base(options)
        {

        }

        public DbSet<TransactionModel> TransactionModels { get; set; }

        public DbSet<Summation> Summations { get; set; }
    }
}

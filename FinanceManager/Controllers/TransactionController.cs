using FinanceManager.Data;
using FinanceManager.Models;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using Microsoft.IdentityModel.Tokens;

namespace FinanceManager.Controllers
{
    public class TransactionController : Controller
    {
        private readonly DataContext _context;
        public TransactionController(DataContext context)
        {
            _context = context;
        }

        public async Task<IActionResult> Index()
        {
            var totalSavings = 0.00m;
            var totalSpending = 0.00m;
            var transactionList = await _context.TransactionModels.ToListAsync();
            var amountSummations = await _context.Summations.FirstOrDefaultAsync(x => x.Id == 1);
            if (amountSummations is not null)
            {
                totalSavings = amountSummations.TotalSavngs;
                totalSpending = amountSummations.TotalSpending;
            }
            ViewData["TotalSavings"] = totalSavings;
            ViewData["TotalSpending"] = totalSpending;
            return View(transactionList);
        }

        [HttpGet]
        public IActionResult Create()
        {
            return View();
        }

        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Create([Bind("Id,Amount,TransactionDate,TransactionType,TransctionNote,TransactionForm")] TransactionModel transaction)
        {
            if (ModelState.IsValid)
            {
                TransactionModel newTransaction = new TransactionModel();
                Summation newSummation = new Summation();

                newTransaction.Amount = transaction.Amount;
                newTransaction.TransactionDate = transaction.TransactionDate;
                newTransaction.TransactionForm = transaction.TransactionForm;
                newTransaction.TransactionType = transaction.TransactionType;
                newTransaction.TransctionNote = transaction.TransctionNote;

                _context.TransactionModels.Add(transaction);
                await _context.SaveChangesAsync();

                var amountSummations = await _context.Summations.FirstOrDefaultAsync(x => x.Id == 1);
                {
                    if (amountSummations is not null)
                    {
                        if (transaction.TransactionForm == TransactionForm.Debit)
                        {
                            amountSummations.TotalSpending = amountSummations.TotalSpending + transaction.Amount;
                            amountSummations.TotalSavngs = amountSummations.TotalSavngs - transaction.Amount;
                        }
                        else
                        {
                            amountSummations.TotalSavngs = amountSummations.TotalSavngs + transaction.Amount;
                        }
                        _context.SaveChanges();
                    }
                    else
                    {
                        Console.WriteLine("Error reading amount summation from the db!");
                    }
                }

                return RedirectToAction("Index");
            }

            return View(transaction);
        }

        [HttpGet]
        public IActionResult Analysis()
        {
            return View();
        }
    }
}

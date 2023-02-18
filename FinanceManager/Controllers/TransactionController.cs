using FinanceManager.Data;
using FinanceManager.Models;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using Microsoft.IdentityModel.Tokens;
using Newtonsoft.Json;

namespace FinanceManager.Controllers
{
    public class TransactionController : Controller
    {
        private readonly DataContext _context;
        private readonly ILogger _logger;
        public TransactionController(DataContext context, ILogger<TransactionController> logger)
        {
            _context = context;
            _logger = logger;
        }

        public async Task<IActionResult> Index()
        {
            _logger.LogInformation($"Call to home route.");
            var totalSavings = 0.00m;
            var totalSpending = 0.00m;
            _logger.LogInformation($"Retriving transaction lists from db server");
            var transactionList = await _context.TransactionModels.ToListAsync();
            _logger.LogInformation($"Retriving amounnt summations from db server.");
            var amountSummations = await _context.Summations.FirstOrDefaultAsync(x => x.Id == 1);
            if (amountSummations is not null)
            {
                totalSavings = amountSummations.TotalSavngs;
                totalSpending = amountSummations.TotalSpending;
            }
            ViewData["TotalSavings"] = totalSavings;
            ViewData["TotalSpending"] = totalSpending;
            _logger.LogInformation($"Rendering transactions list.");
            return View(transactionList);
        }

        [HttpGet]
        public IActionResult Create()
        {
            _logger.LogInformation($"Call to create route");
            return View();
        }

        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Create([Bind("Id,Amount,TransactionDate,TransactionType,TransctionNote,TransactionForm")] TransactionModel transaction)
        {
            string userTransactionData = JsonConvert.SerializeObject(transaction);
            _logger.LogInformation($"User submitted a transaction for recording. Transaaction data: {userTransactionData}", userTransactionData);
            if (ModelState.IsValid)
            {

                TransactionModel newTransaction = new TransactionModel();
                Summation newSummation = new Summation();

                newTransaction.Amount = transaction.Amount;
                newTransaction.TransactionDate = transaction.TransactionDate;
                newTransaction.TransactionForm = transaction.TransactionForm;
                newTransaction.TransactionType = transaction.TransactionType;
                newTransaction.TransctionNote = transaction.TransctionNote;

                _logger.LogInformation($"Saving new record to the db server");
                _context.TransactionModels.Add(transaction);
                await _context.SaveChangesAsync();

                _logger.LogInformation($"Finalizing total amount summations");
                var amountSummations = await _context.Summations.FirstOrDefaultAsync(x => x.Id == 1);
                {
                    if (amountSummations is not null)
                    {
                        if (transaction.TransactionForm == TransactionForm.Debit)
                        {
                            amountSummations.TotalSpending = amountSummations.TotalSpending + transaction.Amount;
                            amountSummations.TotalSavngs = amountSummations.TotalSavngs - transaction.Amount;
                            amountSummations.LastUpdateDate = DateTime.Now;
                        }
                        else
                        {
                            amountSummations.TotalSavngs = amountSummations.TotalSavngs + transaction.Amount;
                            amountSummations.LastUpdateDate = DateTime.Now;
                        }
                        _context.SaveChanges();
                        _logger.LogInformation($"Saved new total amount summations to the db");
                    }
                    else
                    {
                        _logger.LogError($"Error reading amount sumation from the db server.");
                    }
                }
                _logger.LogWarning("Redirecting user to home page.");
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

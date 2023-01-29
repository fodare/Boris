using FinanceManager.Data;
using FinanceManager.Models;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;

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
            var transactionList = await _context.TransactionModels.ToListAsync();
            return View(transactionList);
        }

        [HttpGet]
        public IActionResult Create()
        {
            return View();
        }

        [HttpPost]
        [ValidateAntiForgeryToken]
        public async Task<IActionResult> Create([Bind("Id,Amount,TransactionDate,TransactionType,TransctionNote")] TransactionModel transaction)
        {
            if (ModelState.IsValid)
            {
                _context.TransactionModels.Add(transaction);
                await _context.SaveChangesAsync();
                return RedirectToAction("Index");
            }
            return View(transaction);
        }

    }
}

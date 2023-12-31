using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using backend.Data;
using backend.Models;
using backend.Services;
using Microsoft.AspNetCore.Mvc;

namespace backend.Controllers
{
    [ApiController]
    [Route("api/v2/[controller]")]
    public class TransactionController : ControllerBase
    {
        private readonly ITransactionService _transactionService;
        DataContextDapper _dapper;
        public TransactionController(ITransactionService transactionService)
        {
            _transactionService = transactionService;
            _dapper = new DataContextDapper();
        }

        [HttpGet("health", Name = "HelathCheck")]
        public IActionResult Gethealth()
        {
            _dapper.ExecuteSql<string>("SELECT GETDATE()");
            return Ok(DateTime.Now);
        }
    }
}
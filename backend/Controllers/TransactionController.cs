using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using backend.Models;
using Microsoft.AspNetCore.Mvc;

namespace backend.Controllers
{
    [ApiController]
    [Route("api/v2/[controller]")]
    public class TransactionController : ControllerBase
    {
        public TransactionController()
        {
        }

        [HttpGet("health", Name = "HelathCheck")]
        public IActionResult Gethealth()
        {
            return Ok(DateTime.Now);
        }
    }
}
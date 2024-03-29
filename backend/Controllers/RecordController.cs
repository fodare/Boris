using backend.Dtos;
using backend.Models;
using backend.Services;
using Microsoft.AspNetCore.Mvc;

namespace backend.Controllers
{
    [ApiController]
    [Route("api/v2/[controller]")]
    public class RecordController : ControllerBase
    {
        private readonly IRecordService _recordService;
        public RecordController(IRecordService recordService)
        {
            _recordService = recordService;
        }

        [HttpGet("/recordService", Name = "RecordServiceHome")]
        public ActionResult GetRecordServiceHealth()
        {
            return Ok(DateTime.Now);
        }
    }
}
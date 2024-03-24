// using backend.Dtos;
// using backend.Models;
// using backend.Services;
// using Microsoft.AspNetCore.Mvc;

// namespace backend.Controllers
// {
//     [ApiController]
//     [Route("api/v2/[controller]")]
//     public class TransactionController : ControllerBase
//     {
//         private readonly ITransactionService _transactionService;
//         public TransactionController(ITransactionService transactionService)
//         {
//             _transactionService = transactionService;
//         }

//         [HttpGet("health", Name = "HelathCheck")]
//         public IActionResult Gethealth()
//         {
//             return Ok(DateTime.Now);
//         }

//         [HttpGet("transactionLists", Name = "GetTrasnactions")]
//         public ActionResult<ResponseModel<TransactionModel>> GetTransactionRecords()
//         {
//             ResponseModel<IEnumerable<TransactionModel>> response = new();
//             var transactionsList = _transactionService.GetTransactions();
//             if (transactionsList != null)
//             {
//                 response.Message = "Successfully retrived transaction record list";
//                 response.Success = true;
//                 response.Data = (IEnumerable<TransactionModel>?)transactionsList;
//                 return Ok(transactionsList);
//             }
//             else
//             {
//                 response.Message = "Error fetching transaction records. Please try again!";
//                 response.Success = false;
//                 return StatusCode(500, response);
//             }
//         }

//         [HttpPost("summary", Name = "GetTransactionSummary")]
//         public ActionResult<ResponseModel<SummaryModel>> GetRecordSummary(GetSummaryDTO queryTime)
//         {
//             ResponseModel<IEnumerable<SummaryModel>> response = new();
//             var transactionSummary = _transactionService.GetSummary(queryTime);
//             if (transactionSummary != null && transactionSummary.Any())
//             {
//                 response.Message = "Successfully retrived transaction summary!";
//                 response.Success = true;
//                 response.Data = (IEnumerable<SummaryModel>?)transactionSummary;
//                 return Ok(response);
//             }
//             else if (transactionSummary != null && !transactionSummary.Any())
//             {
//                 response.Message = "Query date range has to value to summarize!";
//                 response.Success = false;
//                 response.Data = (IEnumerable<SummaryModel>?)transactionSummary;
//                 return Ok(response);
//             }
//             else
//             {
//                 response.Success = false;
//                 response.Message = "Error retriving transaction summary. Please try again!";
//                 return StatusCode(500, response);
//             }
//         }

//         [HttpGet("{transactionId}", Name = "GetTransaction")]
//         public ActionResult<ResponseModel<TransactionModel>> GetTransactionById(int transactionId)
//         {
//             ResponseModel<TransactionModel> response = new();
//             var qureiedTransaction = _transactionService.GetTransaction(transactionId);
//             if (qureiedTransaction.TransactionId == transactionId)
//             {
//                 response.Message = "Successfully retrived record";
//                 response.Data = qureiedTransaction;
//                 response.Success = true;
//                 return Ok(response);
//             }
//             else
//             {
//                 response.Message = $"Can not find record with id {transactionId}";
//                 response.Success = false;
//                 return NotFound(response);
//             }
//         }

//         [HttpPost("addtransaction", Name = "RecordTransaction")]
//         public ActionResult<ResponseModel<string>> CreateRecord([FromBody] RecordTransactionDto newRecord)
//         {
//             ResponseModel<string> response = new();
//             bool userAdded = _transactionService.RecordTransaction(newRecord);
//             if (userAdded)
//             {
//                 response.Message = "Transaction aded successfully!";
//                 response.Success = true;
//                 return Ok(response);
//             }
//             else
//             {
//                 response.Message = "Error adding transaction. Please try again!";
//                 response.Success = false;
//                 return BadRequest(response);
//             }

//         }

//         [HttpPut("updateTransaction/{transactionId}", Name = "UpdateRecord")]
//         public ActionResult<ResponseModel<string>> UpdateTransactionRecord(int transactionId,
//             [FromBody] UpdateTransactionDto newRecord)
//         {
//             ResponseModel<string> response = new();
//             bool recordUpdated = _transactionService.UpdateTransactionRecord(newRecord, transactionId);
//             if (recordUpdated)
//             {
//                 response.Success = true;
//                 response.Message = "Transaction record updated successfully!";
//                 return Ok(response);
//             }
//             else
//             {
//                 response.Message = "Error updating record. Please try again";
//                 response.Success = false;
//                 return BadRequest(response);
//             }
//         }
//     }
// }
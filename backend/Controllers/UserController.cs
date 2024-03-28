using AutoMapper;
using backend.Dtos;
using backend.Models;
using backend.Services;
using Microsoft.AspNetCore.Mvc;

namespace backend.Controllers
{
    [ApiController]
    [Route("api/v3/[controller]")]
    public class UserController : ControllerBase
    {
        private readonly IUserService _userService;
        IMapper _mapper;
        public UserController(IUserService userService)
        {
            _userService = userService;
            _mapper = new Mapper(new MapperConfiguration(cfg =>
            {
                cfg.CreateMap<UserModel, GetUserDTO>().ReverseMap();
            }));
        }

        [HttpGet("/", Name = "Home")]
        public ActionResult GetHealth()
        {
            return Ok(DateTime.Now);
        }

        [HttpGet("users", Name = "GetUsers")]
        public ActionResult<ResponseModel<IEnumerable<GetUserDTO>>> GetUserList()
        {
            ResponseModel<IEnumerable<GetUserDTO>> response = new();
            var userList = _userService.GetUsers();
            if (userList is null)
            {
                response.Message = "Error retriving user list. Please try again";
                return BadRequest(response);
            }
            response.Data = _mapper.Map<List<GetUserDTO>>(userList);
            response.Success = true;
            response.Message = "Successfully retrived user list.";
            return Ok(response);
        }

        [HttpPost("user/register", Name = "CreateUser")]
        public ActionResult<ResponseModel<string>> RegisterUser([FromBody] NewUserDTO newUser)
        {
            ResponseModel<string> response = new();
            bool userCreated = _userService.CreateUser(newUser);
            if (userCreated)
            {
                response.Success = true;
                response.Message = "User created successfully!";
                return Ok(response);
            }
            else
            {
                response.Success = false;
                response.Message = "Error creating account. Please try again!";
                Console.WriteLine("Error creating account. Please try again!");
                return BadRequest(response);
            }
        }

        [HttpGet("{userName}", Name = "GetUserByUserName")]
        public ActionResult<ResponseModel<string>> FetchByUserName(string userName)
        {
            ResponseModel<GetUserDTO> response = new();
            try
            {
                var queryResult = _userService.GetUserByUserName(userName);
                if (queryResult != null)
                {
                    response.Message = "Successfully retrived user.";
                    response.Success = true;
                    response.Data = _mapper.Map<GetUserDTO>(queryResult);
                    return Ok(response);
                }
                response.Message = "Error retriving user. Can not find quried user!";
                return BadRequest(response);
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Error fetching user {userName}. Excaption: {ex.Message}");
                response.Message = "Error while fetching qureied user. Please try again!";
                return StatusCode(StatusCodes.Status500InternalServerError, response);
            }
        }

        [HttpGet("userid/{userId}/", Name = "GetUserById")]
        public ActionResult<ResponseModel<GetUserDTO>> GetUser(int userId)
        {
            ResponseModel<GetUserDTO> response = new();
            try
            {
                var queryResult = _userService.GetUserById(userId);
                if (queryResult != null)
                {
                    response.Message = "User record retrived successfully!";
                    response.Data = _mapper.Map<GetUserDTO>(queryResult);
                    response.Success = true;
                    return Ok(response);
                }
                response.Message = "Error while fetching user. Please try again!";
                return BadRequest(response);
            }
            catch (Exception ex)
            {
                response.Message = "Error while fetching user. Please try again!";
                Console.WriteLine($"Error fetching user with id {userId}. Exception {ex.Message}");
                return StatusCode(StatusCodes.Status500InternalServerError, response);
            }
        }

        [HttpPost("verify", Name = "VerifyUser")]
        public ActionResult<ResponseModel<string>> VerifyUserCreds([FromBody] VerifyUserDTO userInfo)
        {
            ResponseModel<string> response = new();
            bool passVerfication = _userService.VerifyUser(userInfo.UserName, userInfo.password);
            if (!passVerfication)
            {
                response.Message = "Verfication failed";
                return BadRequest(response);
            }
            response.Message = "Verification successful!";
            response.Success = true;
            return Ok(response);
        }

    }
}

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
                // cfg.CreateMap<UserModel, GetUserDto>().ReverseMap();
            }));
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

        // [HttpPost("login", Name = ("login"))]
        // public ActionResult<ResponseModel<string>> AuthenticateUser([FromBody] LoginDto userInfo)
        // {
        //     ResponseModel<string> response = new();
        //     if (_userService.VerifyUser(userInfo.UserName, userInfo.Password))
        //     {
        //         response.Success = true;
        //         response.Message = "User authenticated successfully!";
        //         return Ok(response);
        //     }
        //     else
        //     {
        //         response.Success = false;
        //         response.Message = "Error authenticating user. Please try again!";
        //         return BadRequest(response);
        //     }
        // }

        // [HttpGet("user/{userId}", Name = "GetUserById")]
        // public ActionResult<ResponseModel<GetUserDto>> GetUser(int userId)
        // {
        //     ResponseModel<GetUserDto> response = new();
        //     var queryResult = _userService.GetUser(userId);
        //     if (queryResult != null)
        //     {
        //         response.Success = true;
        //         response.Data = _mapper.Map<GetUserDto>(queryResult);
        //         return Ok(response);
        //     }
        //     else
        //     {
        //         return BadRequest("Can not find qureied user!");
        //     }
        // }

        // [HttpGet("{userName}", Name = "ByUserName")]
        // public ActionResult<ResponseModel<GetUserDto>> FetchUserByUserName(string userName)
        // {
        //     ResponseModel<GetUserDto> response = new();
        //     var queryResult = _userService.GetUserByUserName(userName);
        //     if (queryResult != null)
        //     {
        //         response.Success = true;
        //         response.Data = _mapper.Map<GetUserDto>(queryResult);
        //         return Ok(response);
        //     }
        //     else
        //     {
        //         response.Success = false;
        //         response.Message = "Can not find qureied user!";
        //         return BadRequest(response);
        //     }
        // }

        // [HttpGet("users", Name = "GetUserList")]
        // public ActionResult<ResponseModel<GetUserDto>> FetchUser()
        // {
        //     ResponseModel<IEnumerable<GetUserDto>> response = new();
        //     var userList = _userService.GetUsers();
        //     IEnumerable<GetUserDto> filteredUserList = _mapper.Map<List<GetUserDto>>(userList);
        //     response.Message = "Successfully retrived users list";
        //     response.Success = true;
        //     response.Data = filteredUserList;
        //     return Ok(response);
        // }
    }
}
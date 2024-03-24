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

        [HttpGet("{userId}", Name = "GetUserById")]
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
    }

}

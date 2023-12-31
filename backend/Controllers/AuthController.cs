using System;
using System.Threading.Tasks;
using AutoMapper;
using backend.Dtos;
using backend.Models;
using backend.Services;
using Microsoft.AspNetCore.Mvc;

namespace backend.Controllers
{
    [ApiController]
    [Route("api/v2/[controller]")]
    public class AuthController : ControllerBase
    {
        private readonly IUserService _userService;
        IMapper _mapper;
        public AuthController(IUserService userService)
        {
            _userService = userService;
            _mapper = new Mapper(new MapperConfiguration(cfg =>
            {
                cfg.CreateMap<UserModel, GetUserDto>().ReverseMap();
            }));
        }

        [HttpGet("user/{userId}", Name = "GetUserById")]
        public async Task<ActionResult<ResponseModel<GetUserDto>>> GetUserAsync(int userId)
        {
            ResponseModel<GetUserDto> response = new();
            var queryResult = await _userService.GetUser(userId);
            if (queryResult != null)
            {
                response.Success = true;
                response.Data = _mapper.Map<GetUserDto>(queryResult);
                return Ok(response);
            }
            else
            {
                return BadRequest("Can not find qureied user!");
            }
        }

        [HttpPost("user/register", Name = "CreateUser")]
        public async Task<ActionResult> RegisterUser([FromBody] UserRegestration newUser)
        {
            bool userCreated = await _userService.CreateUser(newUser);
            if (userCreated)
            {
                return Ok();
            }
            else
            {
                return BadRequest("Username is taken. Please try with another user name");
            }
        }

        [HttpGet("users", Name = "GetUserList")]
        public async Task<ActionResult<GetUserDto>> FetchUser()
        {
            var userList = await _userService.GetUsers();
            var filteredUserList = _mapper.Map<List<GetUserDto>>(userList);
            return Ok(filteredUserList);
        }
    }
}
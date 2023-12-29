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
        public async Task<ActionResult<GetUserDto>> GetUserAsync(int userId)
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
    }
}
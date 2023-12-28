using System;
using System.Threading.Tasks;
using backend.Dtos;
using backend.Models;

namespace backend.Services
{
    public interface IUserService
    {
        Task<ResponseModel<IEnumerable<User>>> GetUsers();

        Task<ResponseModel<User>> GetUser(int userId);

        Task<ResponseModel<string>> CreateUser(UserRegestration newUser);
    }
}
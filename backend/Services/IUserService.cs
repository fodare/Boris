using System;
using System.Threading.Tasks;
using backend.Dtos;
using backend.Models;

namespace backend.Services
{
    public interface IUserService
    {
        Task<IEnumerable<UserModel>> GetUsers();

        Task<UserModel> GetUser(int userId);

        Task<string> CreateUser(UserRegestration newUser);
    }
}
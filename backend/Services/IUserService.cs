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

        Task<bool> CreateUser(UserRegestration newUser);

        Task<bool> VerifyUser(string userName, string password);
    }
}
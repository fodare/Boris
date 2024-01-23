using System;
using System.Threading.Tasks;
using backend.Dtos;
using backend.Models;

namespace backend.Services
{
    public interface IUserService
    {
        IEnumerable<UserModel> GetUsers();

        UserModel? GetUser(int userId);

        UserModel? GetUserByUserName(string userName);

        bool CreateUser(UserRegestration newUser);

        bool VerifyUser(string userName, string password);
    }
}
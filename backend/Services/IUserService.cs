using System;
using System.Threading.Tasks;
using backend.Dtos;
using backend.Models;

namespace backend.Services
{
    public interface IUserService
    {
        bool CreateUser(NewUserDTO newUser);

        UserModel? GetUserByUserName(string userName);

        UserModel? GetUserById(int userId);

        IEnumerable<UserModel>? GetUsers();

        bool LockUser(int userId);

        bool VerifyUser(string userName, string password);
    }
}
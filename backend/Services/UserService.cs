using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using backend.Data;
using backend.Dtos;
using backend.Models;
using Microsoft.AspNetCore.Hosting.Server;

namespace backend.Services
{
    public class UserService : IUserService
    {
        private readonly DataContextDapper _dapper;
        public UserService()
        {
            _dapper = new DataContextDapper();
        }

        public async Task<bool> CreateUser(UserRegestration newUser)
        {
            try
            {
                string sqlCommand = $@"EXEC FinanceManagerSchema.spUser_Add 
                @userName = '{newUser.UserName}', 
                @userPassword = '{newUser.Password}',
                @createDate = '{DateTime.Now}'";

                bool userAdded = _dapper.ExcecuteSqlAdd(sqlCommand);
                if (userAdded)
                {
                    return true;
                }
                return false;
            }
            catch (Exception e)
            {
                Console.WriteLine($"Error creating user.{e.Message}");
                return false;
            }
        }

        public async Task<UserModel>? GetUser(int userId)
        {
            string sqlCommand = @$"EXEC FinanceManagerSchema.spUser_Get 
                @userId = {userId}";
            UserModel qureiedUser = _dapper.ExecuteSql<UserModel>(sqlCommand);
            if (qureiedUser.UserId > 0)
            {
                return qureiedUser;
            }
            return null;
        }

        public Task<IEnumerable<UserModel>> GetUsers()
        {
            throw new NotImplementedException();
        }
    }
}
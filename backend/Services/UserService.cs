using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using backend.Data;
using backend.Dtos;
using backend.Models;

namespace backend.Services
{
    public class UserService : IUserService
    {
        private readonly DataContextDapper _dapper;
        public UserService()
        {
            _dapper = new DataContextDapper();
        }

        public Task<string> CreateUser(UserRegestration newUser)
        {
            throw new NotImplementedException();
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
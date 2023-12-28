using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using backend.Dtos;
using backend.Models;

namespace backend.Services
{
    public class UserService : IUserService
    {
        public Task<ResponseModel<string>> CreateUser(UserRegestration newUser)
        {
            throw new NotImplementedException();
        }

        public Task<ResponseModel<User>> GetUser(int userId)
        {
            throw new NotImplementedException();
        }

        public Task<ResponseModel<IEnumerable<User>>> GetUsers()
        {
            throw new NotImplementedException();
        }
    }
}
using backend.Data;
using backend.Dtos;
using backend.Helpers;
using backend.Models;

namespace backend.Services
{
    public class UserService : IUserService
    {
        private readonly DataContextDapper _dapper;
        private readonly UserHelper _userHelper;
        public UserService()
        {
            _dapper = new DataContextDapper();
            _userHelper = new UserHelper();
        }

        public bool CreateUser(NewUserDTO newUser)
        {
            static string getServerTime() => DateTime.Now.ToString("yyyy-MM-dd");
            try
            {
                var hashedUserPassword = _userHelper.CreatePasswordHash(newUser.UserPassword);

                string sqlCommand = $@"EXEC FinanceRecordSchema.spUser_Add @userName ='{newUser.UserName}', @userPassword ='{hashedUserPassword}',@isAdmin ={0}, @createDate ='{getServerTime()}', @updateDate = '{getServerTime()}'";

                bool userAdded = _dapper.ExcecuteSqlAdd(sqlCommand);
                if (userAdded)
                {
                    return true;
                }
                return false;
            }
            catch (Exception e)
            {
                Console.WriteLine($"Error creating user record. {e.Message}");
                return false;
            }
        }

        public UserModel? GetUserByUserName(string userName)
        {
            string sqlCommand = @$"EXEC FinanceRecordSchema.spUser_Get @userName = '{userName}'";
            UserModel qureiedUser = _dapper.ExecuteSql<UserModel>(sqlCommand);
            if (qureiedUser.UserId > 0)
            {
                return qureiedUser;
            }
            return null;
        }

        public UserModel? GetUserById(int userId)
        {
            string sqlCommand = @$"EXEC FinanceRecordSchema.spUser_Get @userId = '{userId}'";
            UserModel qureiedUser = _dapper.ExecuteSql<UserModel>(sqlCommand);
            if (qureiedUser.UserId > 0)
            {
                return qureiedUser;
            }
            return null;
        }

        public IEnumerable<UserModel>? GetUsers()
        {
            string sqlCommand = "EXEC FinanceRecordSchema.spUser_Get";
            IEnumerable<UserModel> userList = _dapper.LoadData<UserModel>(sqlCommand);
            return userList;
        }

        public bool LockUser(int userId)
        {
            throw new NotImplementedException();
        }

        public bool VerifyUser(string userName, string password)
        {
            throw new NotImplementedException();
        }
    }
}
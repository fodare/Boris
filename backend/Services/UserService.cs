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
            try
            {
                var hashedUserPassword = _userHelper.CreatePasswordHash(newUser.UserPassword);

                string sqlCommand = $@"INSERT INTO FinanceRecordSchema.UserRecord
                    ([UserName], [UserPassword], [IsAdmin], [CreatedDate],[UpdatedDate])
                    VALUES ( '{newUser.UserName}', '{newUser.UserPassword}', 0, '2023-12-31', '2023-12-31')";

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

        // public UserModel? GetUser(int userId)
        // {
        //     string sqlCommand = @$"EXEC FinanceManagerSchema.spUser_Get 
        //         @userId = {userId}";
        //     UserModel qureiedUser = _dapper.ExecuteSql<UserModel>(sqlCommand);
        //     if (qureiedUser.UserId > 0)
        //     {
        //         return qureiedUser;
        //     }
        //     Console.WriteLine($"Error feting user with id {userId}");
        //     return null;
        // }

        // public UserModel? GetUserByUserName(string userName)
        // {
        //     string sqlCommand = @$"EXEC FinanceManagerSchema.spUser_Get 
        //         @userName = {userName}";
        //     UserModel qureiedUser = _dapper.ExecuteSql<UserModel>(sqlCommand);
        //     if (qureiedUser.UserId > 0)
        //     {
        //         return qureiedUser;
        //     }
        //     Console.WriteLine($"Error feting user with username {userName}");
        //     return null;
        // }

        // public IEnumerable<UserModel>? GetUsers()
        // {
        //     string sqlCommand = $"EXEC FinanceManagerSchema.spUser_Get";
        //     try
        //     {
        //         IEnumerable<UserModel> userList = _dapper.LoadData<UserModel>(sqlCommand);
        //         return userList;
        //     }
        //     catch (Exception e)
        //     {
        //         Console.WriteLine($"Error fetching user list. {e.Message}");
        //         return null;
        //     }

        // }

        // public bool VerifyUser(string userName, string userPassword)
        // {
        //     string sqlCommand = @$"EXEC FinanceManagerSchema.spUser_Get 
        //         @userName = '{userName}'";
        //     UserModel qureidUser = _dapper.LoadDataSingle<UserModel>(sqlCommand);
        //     if (qureidUser.UserName != null)
        //     {
        //         bool passwordMatch = _userHelper.VerifyPasswordHash(userPassword, qureidUser.UserPassword);
        //         if (passwordMatch)
        //         {
        //             return true;
        //         }
        //         Console.WriteLine($"Error verifying user credentails");
        //         return false;
        //     }
        //     else
        //     {
        //         Console.WriteLine($"Erro. User account not found!");
        //         return false;
        //     }
        // }
    }
}
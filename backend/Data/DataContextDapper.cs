using System;
using System.Data;
using System.Data.Common;
using System.Globalization;
using Dapper;
using Microsoft.Data.SqlClient;
using Microsoft.IdentityModel.Tokens;

namespace backend.Data
{
    public class DataContextDapper
    {
        private readonly string? dbConnectionString = Environment.GetEnvironmentVariable("dbConString");
        public DataContextDapper()
        {
            if (dbConnectionString == null)
            {
                throw new NullReferenceException("Db connection string is null. Check the connection string is exported!");
            }
        }

        public T ExecuteSql<T>(string sqlCommand)
        {
            IDbConnection dbConnection = new SqlConnection(dbConnectionString);
            var queryResponse = dbConnection.QuerySingle<T>(sqlCommand);
            return queryResponse;
        }

        public bool ExcecuteSqlAdd(string sqlCommand)
        {
            IDbConnection dbConnection = new SqlConnection(dbConnectionString);
            return dbConnection.Execute(sqlCommand) > 0;
        }

        public IEnumerable<T> LoadData<T>(string sqlCommand)
        {
            IDbConnection dbConnection = new SqlConnection(dbConnectionString);
            return dbConnection.Query<T>(sqlCommand);
        }
    }
}
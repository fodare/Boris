using System.Data;
using Dapper;
using Microsoft.Data.SqlClient;

namespace backend.Data
{
    public class DataContextDapper
    {
        static readonly string? dbServerName = Environment.GetEnvironmentVariable("dbServerName");
        static readonly string? dbName = Environment.GetEnvironmentVariable("dbName");
        static readonly string? dbUserName = Environment.GetEnvironmentVariable("dbUserName");
        static readonly string? dbPassword = Environment.GetEnvironmentVariable("dbPassword");

        static readonly string connectionString = @$"Server={dbServerName};Database={dbName};Trusted_Connection=false;TrustServerCertificate=True;User Id={dbUserName};Password={dbPassword};";

        private readonly string? dbConnectionString = connectionString;

        public DataContextDapper()
        {
            if (!TestDBConnection())
            {
                throw new NullReferenceException(@"DB connection failed. Check the connection string is correct");
            }
            Console.WriteLine("Database connection successful!");
        }

        public bool TestDBConnection()
        {
            using IDbConnection testConnection = new SqlConnection(dbConnectionString);
            Console.WriteLine($"Attempting connection to {dbConnectionString}");
            try
            {
                string sqlCommand = "SELECT GETDATE();";
                var queryResponse = testConnection.Query<string>(sqlCommand);
                if (queryResponse is null)
                {
                    Console.WriteLine("Database connection failed!. Check DB connection string is correct.");
                    return false;
                }
                return true;
            }
            catch (Exception ex)
            {
                Console.WriteLine($"DB connection successful!. Exception {ex.Message}");
                return false;
            }
        }

        public T ExecuteSql<T>(string sqlCommand)
        {
            using IDbConnection dbConnection = new SqlConnection(dbConnectionString);
            var queryResponse = dbConnection.QuerySingle<T>(sqlCommand);
            return queryResponse;
        }

        public bool ExcecuteSqlAdd(string sqlCommand)
        {
            using IDbConnection dbConnection = new SqlConnection(dbConnectionString);
            return dbConnection.Execute(sqlCommand) > 0;
        }

        public IEnumerable<T> LoadData<T>(string sqlCommand)
        {
            using IDbConnection dbConnection = new SqlConnection(dbConnectionString);
            return dbConnection.Query<T>(sqlCommand);
        }

        public T LoadDataSingle<T>(string sqlCommand)
        {
            using IDbConnection dbConnection = new SqlConnection(dbConnectionString);
            return dbConnection.QuerySingle<T>(sqlCommand);
        }
    }
}
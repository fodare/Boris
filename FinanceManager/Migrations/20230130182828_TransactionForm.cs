using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace FinanceManager.Migrations
{
    /// <inheritdoc />
    public partial class TransactionForm : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.AddColumn<decimal>(
                name: "TotalSavings",
                table: "TransactionModels",
                type: "decimal(18,2)",
                nullable: false,
                defaultValue: 0m);

            migrationBuilder.AddColumn<decimal>(
                name: "TotalSpending",
                table: "TransactionModels",
                type: "decimal(18,2)",
                nullable: false,
                defaultValue: 0m);

            migrationBuilder.AddColumn<int>(
                name: "TransactionForm",
                table: "TransactionModels",
                type: "int",
                nullable: false,
                defaultValue: 0);
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropColumn(
                name: "TotalSavings",
                table: "TransactionModels");

            migrationBuilder.DropColumn(
                name: "TotalSpending",
                table: "TransactionModels");

            migrationBuilder.DropColumn(
                name: "TransactionForm",
                table: "TransactionModels");
        }
    }
}

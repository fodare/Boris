# FinanceManager

A personal web-based application to help track spending and savings habits. (Demo only)

<br/>

<img src="https://raw.githubusercontent.com/fodare/media/main/FinanceManager/Home.png" alt="App homepage" title="App homepage">

<br/>

# About
FinanceManager is a web-based .net MVC application to help track personal savings and spending habits. Each spending or savings record is persisted in a connected SQL server. 

The application is intended for personal use and can be hosted on your private machine within your home / private network or a Raspberry PI instance.
<br/>

# Demo Development

### Prerequisite.
- Donet SDK 6+.
- SQL server Express.
- EF CORE and CLI tools.
- Favourite IDE, VS Code or Visual studio.

### Clone and install.

Navigate to your desired dir and run the command below from your favourite CLI tool.

```
git clone https://github.com/fodare/FinanceManager.git
cd FinanceManager/FinanceManager
dotnet build
```

### Edit DB connection string

In the `appsettings.json` file, you can edit the `DefaultConnection` value if you have a different form of authentication to your local SQL server.

### Create first EF core migration and update DB

To help create the first migration and create a database, execute the commands below. You can read more about EF core migration here: [EF CORE Migration Overview](https://learn.microsoft.com/en-us/ef/core/managing-schemas/migrations/?tabs=dotnet-core-cli)

```
dotnet ef migrations add InitialCreate

dotnet ef database update
```

### Run locally 

To start the application on your local machine, execute the command below.

```
dotnet run
```
On your favourite browser navigate to the URL https://localhost:{app listening port} or https://{privatehomeipaddress}:{app listening port}
# FinanceManager

A personal web-based application to help track spending and savings habits. (Demo only)

<br/>

<img src="https://raw.githubusercontent.com/fodare/media/main/FinanceManager/Home.png" alt="App homepage" title="App homepage">

<br/>

# About

FinanceManager is a web-based .net MVC application to help track personal savings and spending habits. Each spending or savings record is persisted in a connected SQL server.

The application is intended for personal use and can be hosted on your private machine within your home / private network or a Raspberry Pi instance.
<br/>

# Demo Development

### Prerequisite

- Donet SDK 7+.
- SQL server Express.
- Dotnet CLI.
- Docker.
- Favorite IDE, VS Code or Visual Studio.

### Clone and install

Navigate to your desired Dir and run the command below from your favorite CLI tool.

```
git clone https://github.com/fodare/FinanceManager.git
cd FinanceManager/FinanceManager
dotnet build
```

### Prepare and configure DB

- Pull / Run an SQL instance [Docker SQL server](<https://hub.docker.com/_/microsoft-mssql-server>).
- Connect to docker container and configure database. DB creation script `DbSetup.sql`.

    ```bash
    docker network ls

    docker network inspect <network name>
    ```

- Configure DB connection string.

    ```bash
    export dbConString='Server=<sqlserver ipaddress>;Database=FinanceManagerDb;Trusted_Connection=false;TrustServerCertificate=True;User Id=<db username>;Password=<db password>'
    ```

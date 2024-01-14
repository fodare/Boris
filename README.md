# FinanceManager

A personal web-based application to help track spending and savings habits. (Demo only)

<img src="https://raw.githubusercontent.com/fodare/media/main/FinanceManager/Home.png" alt="App homepage" title="App homepage">

## About

FinanceManager is a web-based .net MVC application to help track personal savings and spending habits. Each spending or savings record is persisted in a connected SQL server.

The application is intended for personal use and can be hosted on your private machine within your home / private network or a Raspberry Pi instance.

## Prerequisite

- Donet SDK 7+ Installed.
- SQL server Express running.
- Dotnet CLI installed.
- Docker installed.
- Favorite IDE, VS Code or Visual Studio.

## Clone app files

Navigate to your desired Dir and run the command below from your favorite CLI tool.

    ```
    git clone https://github.com/fodare/FinanceManager.git
    cd FinanceManager
    ```
The parent Dir contains a `backend` and a `frontend` sub Dir. `backend` holds the backend API while `frontend` Dir holds a Flask API to serve HTML pages or views.

## Prepare and configure DB

- Pull / Run an SQL instance [Docker SQL server](<https://hub.docker.com/_/microsoft-mssql-server>).
- Connect to docker container and configure database. DB creation script `DbSetup.sql`. DB explorer such as Azure data studio, VS Code SQL server plugin or SQL server management studio (SSMS) provide options to connect to the SQL server instance and execute the `DbSetup.sql` script.

- Configure and export DB connection string.

    ```bash
    docker network ls
    docker network inspect <network name>
    ```

    The command above exposes the `IP address for the server container`. Copy and update the connection string below. Export the database connection string as it's required for backend API to connect to the database.

    ```bash
    export dbConString='Server=<sqlserver ipaddress>;Database=FinanceManagerDb;Trusted_Connection=false;TrustServerCertificate=True;User Id=<db username>;Password=<db password>'
    ```

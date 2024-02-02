# FinanceManager

A personal web-based application to help track spending and savings habits. (Demo version)

<img src="https://github.com/fodare/media/blob/main/FinanceManager/App_home_page.png?raw=true" alt="App homepage" title="App homepage">

## About

FinanceManager is a web-based application to help track personal savings and spending habits. Each spending or savings record is persisted in a connected SQL server.

The application is intended for personal use and can be hosted on your private machine within your home / private network or a Raspberry Pi instance.

## Prerequisite

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

    ```bash
    # Example
    docker run -e "ACCEPT_EULA=Y" -e "MSSQL_SA_PASSWORD=<desired db password>"
    -e "MSSQL_PID=Evaluation" --network host --name sqlserver 
    --hostname sqlserver 
    -d mcr.microsoft.com/mssql/server:2022-preview-ubuntu-22.04

    # Note the SQL server container is exposed to all services within your LAN.
    # You can access the SQL server from another host in the LAN  via the -
    # IP address of the host running the container.
    ```

- Using a DB explorer such as Azure data studio, VS Code SQL server plugin or SQL server management studio (SSMS) provide options to connect to the SQL server instance and execute the `DbSetup.sql` script to help configure the db table.

- Prepare DB connection string.

    ```bash
    # On the host running the SQL server container. Run the command below.
    ip address show
    # You looking for inet 192.168...
    ```

    The command above exposes the `IP address of the container running the SQL server`. Copy and update the connection string below as it's required for the backend API to connect to the database.

    ```bash
    # exmple dbConString="Server=192.168.0.1;Database=FinanceManagerDb;Trusted_Connection=false;TrustServerCertificate=True;User Id=<db username>;Password=<db password>;"
   dbConString="Server=<host ip adress>;Database=FinanceManagerDb;Trusted_Connection=false;TrustServerCertificate=True;User Id=<db username>;Password=<db password>;"
    ```

## Update container environment variable

Update environment varibales place holder in the `.env` file.

- `dbConString`: the database connection string that was prepared in `Prepare and configure DB`
- `secret`: You desired frontend cookies signing secret.
- `host_ip`: You local machine Ip address. Eg 192.168.0.1
- `backendapi_port`: Host listening port number for the backend API service.
- `frontendapi_port`: Host listening port number for the frontendapi service.

## Start services

From your CLI / terminal, ensure you are in the project root dir then execute the command below.

``` bash
docker compose up -d 
```

Visit [localhost:frontendapi_portnumber](<http://localhost:{frontendapi_port number}/>)(e.g <http://localhost:3001>) to access the frontendapi service.

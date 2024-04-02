# FinanceManager

A personal web-based application to help track spending and savings habits. (Demo version)

<img src="https://github.com/fodare/media/blob/main/FinanceManager/App_home_page.png?raw=true" alt="App homepage" title="App homepage">

## About

FinanceManager is a web-based application to help track personal savings and spending habits. Each spending or savings record is persisted in a connected SQL server.

The application is intended for personal use and can be hosted on your private machine within your home / private network or a Raspberry Pi instance.

Below is the web app request flow.

<img src="https://raw.githubusercontent.com/fodare/media/main/FinanceManager/Requestflow.png" alt="App homepage" title="App homepage">

## Prerequisite

- SQL server Express running.
- Dotnet CLI installed.
- Docker installed.
- Favourite IDE, VS Code or Visual Studio.

## Clone app files

Navigate to your desired DIR and run the command below from your favourite CLI tool.

    ```
    git clone https://github.com/fodare/FinanceManager.git
    cd FinanceManager
    ```
The parent DIR contains a `backend` and a `frontend` sub DIR. `backend` holds the backend API while `frontend` DIR holds a Flask API to serve HTML pages or views.

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

- Using a DB explorer such as Azure data studio, VS Code SQL server plugin or SQL server management studio (SSMS) provide options to connect to the SQL server instance and execute the `DbSetup.sql` script to help configure the DB table.

## Update container environment variables

Update environment variables placeholder in the `.env` file.

- `dbServerName`: SQL server name / host ip
- `dbName`: SQL server database name.
- `dbUserName`: SQL server encryptionuser name.
- `dbPassword`: SQL server db password.
- `secret`: Secret key for `frontendapi` sessions.
- `host_ip`: Host  ip address.
- `backendapi_port`: Port to access backendapi.
- `frontendapi_port`: Port to access frontendapi.

## Start services

From your CLI / terminal, ensure you are in the project root DIR then execute the command below.

``` bash
docker compose up -d 
```

Visit [localhost:frontendapi_portnumber](<http://localhost:{frontendapi_port number}/>)(e.g <http://localhost:3001>) to access the frontend service.

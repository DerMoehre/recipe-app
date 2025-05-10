# Recipe Application

This project is a recipe application developed using the following technologies:

* **Frontend:** Angular
* **Backend:** Python with FastAPI
* **Database:** PostgreSQL (in Docker)

## Folder Structure
* `backend/`
    * `app/`
        * `__init__.py`
        * `main.py`
        * `models/`
        * `database.py`
        * `routers/`
        * `schemas/`
    * `Dockerfile`
    * `requirements.txt`
* `database/`
    * `Dockerfile`
* `docker-compose.yml`
* `.env`
* `.gitignore`
* `README.md`

## Getting Started

To set up the development environment, ensure you have the following installed:

* **Docker:** For containerizing the database and backend. You can download and install Docker Desktop from [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/).
* **Git:** For version control.

### Starting the Backend (with Docker Compose)

The recommended way to start the backend and database in the development environment is using Docker Compose:

1.  Navigate to the project's root directory in your terminal.
2.  Run the following command:

    ```bash
    docker-compose up -d --build backend db
    ```

    * `docker-compose up`: Starts the services defined in the `docker-compose.yml` file.
    * `-d`: Starts the containers in detached (background) mode.
    * `--build backend db`: Rebuilds the Docker images for the backend and database if the `Dockerfile` or dependencies have changed.

3.  Once started, the backend will be accessible at `http://localhost:8000` (this can be configured in the `docker-compose.yml`). The PostgreSQL database will be running on `localhost:5432`.

### Database Connection (for Development)

For connecting to the PostgreSQL database in the development environment, use the following information:

* **Host:** `localhost` or `127.0.0.1`
* **Port:** `5432`
* **Database:** The value set for `POSTGRES_DB` in your `.env` file.
* **User:** The value set for `POSTGRES_USER` in your `.env` file.
* **Password:** The value set for `POSTGRES_PASSWORD` in your `.env` file.

Use a database tool like DBeaver to connect to the database and inspect tables or data.

### Test Data

Currently, the database does not contain any initial test data. You can:

* Manually insert data using a database tool (e.g., DBeaver).
* Create SQL scripts and execute them against the database.
* Implement seed functions in your backend to generate test data programmatically.

# Recipe Application

This project is a recipe application developed using the following technologies:

* **Frontend:** Angular
* **Backend:** Python with FastAPI
* **Database:** SQLlite (in Docker)

## Folder Structure
* `backend/`
    * `app/`
        * `__init__.py`
        * `main.py`
        * `models.py`
        * `database.py`
        * `routers.py`
        * `schemas.py`
    * `app.db`
    * `Dockerfile`
    * `requirements.txt`
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
    docker-compose up -d --build backend
    ```

    * `docker-compose up`: Starts the services defined in the `docker-compose.yml` file.
    * `-d`: Starts the containers in detached (background) mode.
    * `--build backend`: Rebuilds the Docker images for the backend

3.  Once started, the backend will be accessible at `http://localhost:8000` (this can be configured in the `docker-compose.yml`).


### Test Data

For development, there are two endpoint routes to insert and delete test data to the db

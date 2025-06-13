
# 🧮 RPN Calculator API – FastAPI + Docker + PostgreSQL

## 🎯 Objective

This project proposes the creation of a **REST API for a Reverse Polish Notation (RPN) calculator**.
The goal is to help our users perform complex calculations while keeping a history of operations in a database.
The application should also allow for **CSV export** of results.

The project is divided and managed according to a **Scrum** methodology with **tickets estimated in Fibonacci story points**.

---

## 📦 Features

- RPN Calculation (Reverse Polish Notation)
- FastAPI REST API
- PostgreSQL Storage
- CSV Export
- Docker Containerization with Docker Compose

---

## 📅 Duration & Organization

- **Single Sprint**: 9 days
- **Start**: Monday, June 16, 2025
- **End**: Thursday, June 26, 2025
- **Daily Stand-ups**: 15 minutes every morning at 9:45 AM
- **Sprint Review**: Thursday, June 26, 2025, at 4:00 PM
- **Sprint Retrospective**: Thursday, June 26, 2025, at 4:30 PM

> 🎲 1 Story Point = 1 day of work
>
> Fibonacci sequence used: 1, 2, 3, 5, 8...

---

## 🧑‍🤝‍🧑 Project Team

We assume that the Tech Lead will also take on the role of Scrum Master and DevOps Engineer and there is only one other developer.

| Role           | Name / Reference            | Main Missions                               |
|----------------|-----------------------------|---------------------------------------------|
| Tech Lead      | [Dieuveille BOUSSA]                  | Architecture, reviews, business guidance    |
| Dev Backend    | Junior Python Developer     | Implementation of the algorithm, API        |
| DevOps         | Infrastructure Engineer / Tech Lead     | Docker, PostgreSQL, CI/CD                   |
| Scrum Master   | Scrum Master / Tech Lead    | Progress tracking, daily, coordination      |

---

## 📋 Key Responsibilities

### 👨‍💻 Tech Lead Python

- Technical choices (FastAPI, PostgreSQL, SQLAlchemy, etc.)

- Code review and pair programming (refactoring, best practices)

- Ensuring code quality (unit tests, integration tests)

- Ensuring SOLID, KISS, YAGNI principles

- Defining modular architecture: separation of layers (API, services, persistence, etc.)

### 🧑‍🏫 Scrum Master

- Facilitation of daily stand-ups, sprint planning & retrospectives

- Monitoring of the burn-down chart

- Setting up the kanban/scrum board (e.g., Jira, Notion, Trello)

### 🧑‍💻 DevOps Engineer

- Writing Dockerfiles

- Configuring docker-compose

- Configuring PostgreSQL, managing volumes

- CI/CD (e.g., GitHub Actions)

---

## 🧱 Technical Organization

### 📁 Clean Architecture Structure (inspired by SOLID)

```arduino
FASTAPI-RPN-Calculator/
├── .github/                 # GitHub configuration
├── ├── workflows/           # GitHub Actions workflows
├── │   ├── ci-dev.yml       # CI workflow for dev branch
├── │   ├── ci-main.yml      # CI workflow for main branch
├── app/
├── ├── api/                 # FastAPI routes
├── │   ├── routes.py
├── ├── core/                # business logic (RPN calculation)
├── │   ├── rpn.py
├── ├── db/                  # ORM models, sessions
├── │   ├── database.py
├── ├── fixtures/            # Test fixtures
├── │   ├── seed.json
├── │   ├── load_fixtures.py
├── ├── models/              # ORM models, sessions
├── │   ├── models.py
├── ├── schemas/             # Pydantic schemas
├── │   ├── schemas.py
├── ├── services/            # business services
├── │   ├── services.py
├── tests/
├── ├── test_database.py
├── ├── test_models.py
├── ├── test_routes.py
├── ├── test_rpn.py
├── ├── test_services.py
├── .env
├── docker-compose.yml
├── Dockerfile
├── example.env
├── main.py
├── pytest.ini
├── README.md
├── requirements.txt
├── wait-for-db.sh
```

---

## 🗂️ Ticket Breakdown

| ID    | Title                                      | Story Points | Due Date  | Acceptance Criteria |
|-------|--------------------------------------------|--------------|-----------|---------------------|
| T1    | Project Initialization + Clean Structure     | 1 SP         | 16/06     | FastAPI project structured into folders `api`, `core`, `schemas`, etc. `.env` file in place |
| T2    | Implementation of RPN Algorithm            | 1 SP         | 16/06     | The function `rpn_calculator(expr)` handles `+`, `-`, `*`, `/` and returns the correct result |
| T3    | Creation of Pydantic Schemas               | 1 SP         | 17/06     | The schemas `OperationRequest` and `OperationResponse` correctly validate inputs |
| T4    | Route POST /calculate                      | 1 SP         | 17/06     | Receives an expression, returns a JSON with the result. Handles errors |
| T5    | Creation of SQLAlchemy ORM Models          | 1 SP         | 18/06     | Model `Operation(id, expression, result)` persisted via PostgreSQL |
| T6    | Addition of Persistence Service             | 2 SP         | 19/06     | Results well stored and retrieved from the database after a calculation |
| T7    | Route GET /export (CSV)                    | 1 SP         | 20/06     | CSV file well generated with columns `ID, Expression, Result`, downloadable |
| T8    | Dockerization of FastAPI App               | 2 SP         | 24/06     | Functional Dockerfile. Starts with `uvicorn` from Docker |
| T9    | docker-compose for PostgreSQL + API       | 2 SP         | 24/06     | `docker-compose up` starts the API and the DB with local persistence |
| T10   | Unit Tests + CI Integration GitHub and Technical Documentation (README + Swagger) | 2 SP         | 26/06     | Tests for calculation, API routes, errors. CI integrated with `pytest` via GitHub Action Complete README, endpoints documented via `/docs` (Swagger) |

---

## ✅ Global Success Criteria

- All tickets validated
  - All tests pass for each feature
- Complete and up-to-date documentation
- Functional project via `http://localhost:8000/docs`
- Results persisted in PostgreSQL
- Dockerized and executable via `docker-compose`
- Minimum test coverage on calculation and endpoints
  - Test coverage above 90%
- Complete and readable CSV export

---

## 🔧 Quick Start

### 📦 Prerequisites

- Docker / Docker Compose
- Python 3.10+
- PostgreSQL 12+ / SQLAlchemy / SQLite (for testing)
- FastAPI
- Python package manager: pip / poetry
- Virtual environment (optional but recommended)
- Git

### 📂 Accessing Endpoints

- **Swagger Documentation**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **API**: [http://localhost:8000](http://localhost:8000)

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/DieuveilleWebH3/fastapi-rpn-calculator.git
   cd fastapi-rpn-calculator
   ```

   Or via SSH

   ```bash
   git clone git@github.com:DieuveilleWebH3/fastapi-rpn-calculator.git
   cd fastapi-rpn-calculator
   ```

2. **Create a `.env` file**

   ```bash
   cp example.env .env
   ```

   Replace the values in the `.env` file with the right and appropriate values.

---

#### 🐍 Virtual Environment Setup

##### Using Poetry: Activate a virtual environment

   1. **Install Poetry if not already installed**

      ```bash
      curl -sSL https://install.python-poetry.org | python3 -
      ```

   2. **Ensure Poetry is in your PATH**

      ```bash
      export PATH="$HOME/.local/bin:$PATH"
      ```

   3. **Install dependencies**

      ```bash
      poetry install
      ```

   4. **Activate the virtual environment**

      ```bash
      poetry shell
      ```

##### Using Pip: Activate a virtual environment

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

1. **Install dependencies**

   **Dev & Prod Environment**

      ```bash
      pip install -r requirements.txt
      ```

#### 🚀 Running the Application

1. **Start the FastAPI server**

   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```

2. **Access the Swagger UI**

   Open your browser and go to [http://localhost:8000/docs](http://localhost:8000/docs) to access the interactive API documentation.

#### 🐳 Running with Docker

1. **Build the Docker image**

   ```bash
   docker build -t fastapi-rpn-calculator .
   ```

2. **Run the Docker container**

   ```bash
   docker run -d -p 8000:8000 fastapi-rpn-calculator
   ```

3. **Running Commands Inside Container**

   ```bash
   docker exec -it <container_id> /bash
   ```

### 🧪 Testing Locally

#### Testing Setup

1. **Add dummy data to test locally**

   ```bash
   export PYTHONPATH=/app
   python app/fixtures/load_fixtures.py
   ```

2. **Run unit tests**

   ```bash
   pytest
   ```

    **Run pytest with coverage**

    ```bash
    pytest --cov=app --cov-report=term-missing
    ```

    **OR**

    ```bash
    pytest --cov=app --cov-report=html
    ```

#### 🧮 Calculate RPN Expression

```bash
curl -X POST "http://localhost:8000/calculate" -H "Content-Type: application/json" -d '{"expression": "5 1 2 + 4 * + 3 -"}'
```

Expected response:

```json
{
  "expression": "5 1 2 + 4 * + 3 -",
  "result": 14.0
}
```

#### 📁 Export CSV

```bash
curl -X GET "http://localhost:8000/export" -H "Accept: text/csv"
```

Expected response: downloadable CSV file with the performed operations.

### 🤝 Contributions

For any contribution, please:

Create a branch with the same name as the ticket `rpn-t<ID>`
Each commit must be linked to a Jira ticket and follow the format `rpn-t<ID> - Commit description`
Make a PR to the `dev` branch

Follow the code style (Black formatting + type hints)

Write unit tests for any business logic

To run the project locally, create a virtual environment and a `.env` file at the root and replace the default values (make sure you have PostgreSQL installed and running):

```bash
cp example.env .env
```

For a local PostgreSQL database, you can use the following settings in your `.env` file after creating the database rpn_db:

```env
POSTGRES_USER=POSTGRES_USER
POSTGRES_PASSWORD=POSTGRES_PASSWORD
POSTGRES_DB=rpn_db
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
DATABASE_URL=postgresql://POSTGRES_USER:POSTGRES_PASSWORD@localhost:5432/rpn_db
```

PS:

- Make sure to have the dependencies installed via `pip install -r requirements.txt` or `poetry install` before starting the project.

- Containerization with Docker will be done in collaboration with the DevOps Engineer/Tech Lead for skill development.

---

### Common Issues

#### Docker cannot access local host PostgreSQL Database

1. **Verify PostgreSQL Host**

   The localhost in your Docker container refers to the container itself, not your host machine.
   If PostgreSQL is running on your host machine, you need to use the host's IP address or host.docker.internal (on Docker Desktop for Windows/Mac).

   <br>

   Update your .env file to use host.docker.internal for DB_HOST:

   ```bash
   DB_HOST=host.docker.internal
   ```

2. **Expose PostgreSQL to the Docker Container**

   Ensure PostgreSQL is configured to accept connections from the Docker container.

   <br>

   Edit pg_hba.conf: Locate the pg_hba.conf file (usually in the PostgreSQL data directory) and add the following line:

   ```bash
   host    all             all             0.0.0.0/0            md5
   ```

   Edit postgresql.conf: Locate the postgresql.conf file and ensure the listen_addresses setting includes *:

   ```bash
   listen_addresses = '*'
   ```

   Restart PostgreSQL: Restart the PostgreSQL service to apply the changes:

   ```bash
   sudo systemctl restart postgresql
   ```

   NB:

   Allowing 0.0.0.0/0 in pg_hba.conf exposes the database to all networks. Consider restricting the CIDR to specific IP ranges or use Docker network aliases to limit access.

   ```bash
   host    all             all             192.168.0.0/16            md5
   ```

   ⚠️ Note: This configuration is for development purposes only. Replace 192.168.0.0/16 with the specific IP range of your Docker network or private network. Do not use 0.0.0.0/0 in production environments as it exposes the database to all networks.

---

## 📝 TODO

- [ ] Separate Dev and Prod Environments (Dockerfiles, docker-compose)

- [ ] Add a logging system (e.g., using Python's logging module or a third-party service)

- [ ] Add lintering and formatting tools (Black, Ruff, mypy)

- [ ] Add more actions to the CI/CD pipeline (e.g., Docker build, push to registry, deploy to staging)

- [ ] Define a staging environment for testing before production deployment

- [ ] Delimit use of API endpoints (e.g., rate limiting, authentication)

---

## 👨‍🔧 Maintainer

Tech Lead : Dieuveille BOUSSA
Contact : [dieuveille.boussa@projet.dev](mailto:dieuveille.boussa@projet.dev)

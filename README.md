
# 🧮 RPN Calculator API – FastAPI + Docker + PostgreSQL

## 🎯 Objective

This project proposes the creation of a **REST API for a Reverse Polish Notation (RPN) calculator**.
The goal is to help our users perform complex calculations while keeping a history of operations in a database.
The application should also allow for **CSV export** of results.

The project is divided and managed according to a **Scrum** methodology with **tickets estimated in Fibonacci story points**.

---

## 📅 Duration & Organization

- **Single Sprint**: 8 days
- **Start**: Monday, June 16, 2025
- **End**: Wednesday, June 25, 2025

> 🎲 1 Story Point = 1 day of work
>
> Fibonacci sequence used: 1, 2, 3, 5, 8...

---

## 🧑‍🤝‍🧑 Project Team

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

- Code review and pair programming

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
app/
├── github/              # GitHub integration (actions, workflows)
│   ├── workflows/
│   │   ├── ci.yml
├── api/                 # FastAPI routes
│   ├── routes.py
├── core/                # business logic (RPN calculation)
│   ├── rpn.py
├── db/                  # ORM models, sessions
│   ├── database.py
├── models/              # ORM models, sessions
│   ├── models.py
├── schemas/             # Pydantic schemas
│   ├── schemas.py
├── services/            # business services
│   ├── services.py
tests/
├── test_database.py
├── test_integration.py
├── test_models.py
├── test_routes.py
├── test_rpn.py
├── test_services.py
.env
Dockerfile
example.env
main.py
pytest.ini
README.md
requirements.txt
```

## 📦 Features

- RPN Calculation (Reverse Polish Notation)
- FastAPI REST API
- PostgreSQL Storage
- CSV Export
- Docker Containerization with Docker Compose

---

## 🗂️ Ticket Breakdown

| ID    | Title                                      | Story Points | Due Date  | Acceptance Criteria |
|-------|--------------------------------------------|--------------|-----------|---------------------|
| T1    | Project Initialization + Clean Structure     | 1 SP         | 16/06     | FastAPI project structured into folders `api`, `core`, `schemas`, etc. `.env` file in place |
| T2    | Implementation of RPN Algorithm            | 2 SP         | 17/06     | The function `rpn_calculator(expr)` handles `+`, `-`, `*`, `/` and returns the correct result |
| T3    | Creation of Pydantic Schemas               | 1 SP         | 17/06     | The schemas `OperationRequest` and `OperationResponse` correctly validate inputs |
| T4    | Route POST /calculate                      | 2 SP         | 18/06     | Receives an expression, returns a JSON with the result. Handles errors |
| T5    | Creation of SQLAlchemy ORM Models          | 2 SP         | 18/06     | Model `Operation(id, expression, result)` persisted via PostgreSQL |
| T6    | Addition of Persistence Service             | 3 SP         | 19/06     | Results well stored and retrieved from the database after a calculation |
| T7    | Route GET /export (CSV)                    | 2 SP         | 20/06     | CSV file well generated with columns `ID, Expression, Result`, downloadable |
| T8    | Dockerization of FastAPI App               | 2 SP         | 21/06     | Functional Dockerfile. Starts with `uvicorn` from Docker |
| T9    | docker-compose for PostgreSQL + API       | 3 SP         | 22/06     | `docker-compose up` starts the API and the DB with local persistence |
| T10   | Technical Documentation (README + Swagger) | 1 SP         | 23/06     | Complete README, endpoints documented via `/docs` (Swagger) |
| T11   | Export CSV: Functional Tests                | 1 SP         | 24/06     | CSV validated, tested with at least 5 expressions in the database |
| T12   | Unit Tests + CI Integration GitHub         | 3 SP         | 25/06     | Tests for calculation, API routes, errors. CI integrated with `pytest` via GitHub Actions |

---

## ✅ Global Success Criteria

- All tickets validated
  - All tests pass for each feature
- Complete and up-to-date documentation
- Functional project via `http://localhost:8000/docs`
- Results persisted in PostgreSQL
- Dockerized and executable via `docker-compose`
- Minimum test coverage on calculation and endpoints
- Complete and readable CSV export

---

## 🔧 Quick Start

### 📦 Prerequisites

- Docker / Docker Compose
- Python 3.10+ (for local testing)
- Git

### 📂 Accessing Endpoints

- **Swagger Documentation**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **API**: [http://localhost:8000](http://localhost:8000)

### 🧪 Testing Locally

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

### 📁 Export CSV

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

- Make sure to have the dependencies installed via `pip install -r requirements.txt` before starting the project.

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

### 👨‍🔧 Maintainer

Tech Lead : Dieuveille BOUSSA
Contact : [dieuveille.boussa@projet.dev](mailto:dieuveille.boussa@projet.dev)

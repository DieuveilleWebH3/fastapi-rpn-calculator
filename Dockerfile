FROM python:3.10-slim

# Disable Poetry virtualenvs
ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR /app

# Install netcat for wait-for-db.sh and system dependencies
RUN apt-get update && apt-get install -y netcat-openbsd curl build-essential libpq-dev && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 - && \
    ln -s $HOME/.local/bin/poetry /usr/local/bin/poetry && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy only the dependency files first for caching
COPY pyproject.toml .
COPY poetry.lock .

# Install dependencies
RUN poetry install --no-interaction --no-root

COPY . .

EXPOSE 8000

RUN chmod +x wait-for-db.sh

CMD ["./wait-for-db.sh", "poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

FROM python:3.10-slim

WORKDIR /app

# Install netcat for wait-for-db.sh
RUN apt-get update && apt-get install -y netcat-openbsd && apt-get clean

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

RUN chmod +x wait-for-db.sh

CMD ["./wait-for-db.sh", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

#!/bin/sh
echo "⏳ Waiting for PostgreSQL..."

MAX_RETRIES=30
RETRY_COUNT=0
while ! nc -z "$POSTGRES_HOST" "$POSTGRES_PORT"; do
  RETRY_COUNT=$((RETRY_COUNT + 1))
  if [ "$RETRY_COUNT" -ge "$MAX_RETRIES" ]; then
    echo "❌ PostgreSQL is not available after $MAX_RETRIES attempts. Exiting."
    exit 1
  fi
  sleep 1
done

echo "✅ PostgreSQL is up. Starting app..."
exec "$@"

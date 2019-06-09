#!/bin/sh

set -e

if env | grep -q "DATABASE_URL"
    then
    until PGPASSWORD="$POSTGRES_PASSWORD" psql -h "$POSTGRES_HOST" -U "$POSTGRES_USER" -c '\q'; do
      >&2 echo "Postgres is unavailable - sleeping"
      sleep 1
    done

    >&2 echo "Postgres is up - Ready to run flask"
fi

source venv/bin/activate

if [[ $# -eq 0 ]]; then
  flask db upgrade
  exec flask run --host=0.0.0.0 
fi

exec "$@"


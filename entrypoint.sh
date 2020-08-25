#!/bin/sh

set -e

if env | grep -q "DATABASE_URL"
    then
    until psql "$DATABASE_URL" -c '\q'; do
      >&2 echo "Postgres is unavailable - sleeping"
      sleep 1
    done

    >&2 echo "Postgres is up - Ready to run flask"
fi

source "$VIRTUAL_ENV"/bin/activate

if [[ $# -eq 0 ]]; then
  flask db upgrade

  if [[ "$FLASK_ENV" = "production" && "$FLASK_CONFIG" = "production" ]]; then
    exec gunicorn -b 0.0.0.0:${PORT:-5000} vedetra-server:app
  else
    exec flask run --host=0.0.0.0 
  fi
fi

exec "$@"


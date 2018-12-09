#!/bin/sh

set -e

source venv/bin/activate

if [[ $# -eq 0 ]]; then
  exec flask run --host=0.0.0.0 
fi

exec "$@"


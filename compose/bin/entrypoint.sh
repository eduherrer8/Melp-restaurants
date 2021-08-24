#!/bin/bash
set -e
while ! nc -z ${DB_HOST} ${DB_PORT}; do
    >&2 echo "Postgres is unavailable - waiting"
    sleep 1
done
>&2 echo "Postgres is up - executing next command"
python manage.py collectstatic --noinput
python manage.py migrate
python manage.py runserver 0.0.0.0:${PORT}



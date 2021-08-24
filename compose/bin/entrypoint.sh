#!/bin/bash
set -e

if [ $ENVIRONMENT == "local" ];
then
    while ! nc -z ${DB_HOST} ${DB_PORT}; do
        >&2 echo "Postgres is unavailable - waiting"
        sleep 1
    done
    >&2 echo "Postgres is up - executing next command"
    python manage.py collectstatic --noinput
    python manage.py migrate
    python manage.py runserver 0.0.0.0:${PORT}
else
    python manage.py migrate
    gunicorn melp.wsgi:application --reload --bind 0.0.0.0:$PORT
fi


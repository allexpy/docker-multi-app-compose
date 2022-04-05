#!/bin/bash

# Check if Postgres is healthy before applying the migrations and running the Django development server.
if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
        sleep 0.1
    done

    echo "PostgreSQL started"
fi


python manage.py migrate --noinput
python manage.py createsuperuser --noinput

RUN_PORT=${PORT:-8085}
/usr/local/bin/gunicorn application.wsgi:application --bind "0.0.0.0:${RUN_PORT}"

exec "$@"

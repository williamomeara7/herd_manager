

#!/bin/bash


SUPER_USER_EMAIL=${DJANGO_SUPER_USER_EMAIL:-"william.omeara123@gmail.com"}


/opt/venv/bin/python manage.py migrate --noinput

/opt/venv/bin/python manage.py migrate --run-syncdb --noinput


# /opt/venv/bin/python manage.py makemigrations --noinput



APP_PORT=${PORT:-8000}

cd /app/
/opt/venv/bin/python manage.py createsuperuser --email $SUPER_USER_EMAIL --noinput || true

/opt/venv/bin/gunicorn --worker-tmp-dir /dev/shm herd_manager.wsgi:application --bind "0.0.0.0":${APP_PORT}
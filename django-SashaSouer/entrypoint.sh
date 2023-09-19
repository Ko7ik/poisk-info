#!/bin/sh
# until python manage.py migrate --noinput; do echo "Waiting for db to be ready..."; sleep 2; done;
echo "Migrate...";
python manage.py makemigrations --noinput;
python manage.py migrate --noinput;
echo "Createsuperuser...";
python manage.py createsuperuser --noinput;
exec "$@";
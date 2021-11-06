#!/bin/sh
wget -qO- https://raw.githubusercontent.com/eficode/wait-for/v2.1.3/wait-for | sh -s -- postgres:5432 -- echo success &
python manage.py collectstatic --no-input &
python manage.py migrate &
python manage.py createsuperuser --noinput &
python manage.py runserver 0.0.0.0:8000
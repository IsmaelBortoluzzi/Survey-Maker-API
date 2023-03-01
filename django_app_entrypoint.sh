#!/bin/bash

python manage.py collectstatic --noinput
python manage.py migrate
gunicorn --bind :8000 --workers 3 surveymaker.wsgi:application
#!/usr/bin/env sh

# Migrate if need
python3 src/manage.py makemigrations
python3 src/manage.py migrate

gunicorn --chdir src/ --workers 2 --bind 0.0.0.0:8000 --log-level debug core.wsgi

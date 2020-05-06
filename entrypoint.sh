#!/bin/bash
set -e

cp .env.example .env
python3 manage.py makemigrations student
python3 manage.py migrate student
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000

exec "$@"
#!/bin/bash
set -e
echo "Running database migrations..."
./scripts/manage.sh make
./scripts/manage.sh migrate
echo "Starting application..."

python manage.py shell < scripts/create_superuser.py
python manage.py runserver 0.0.0.0:8000

#!/bin/bash
set -e

python manage.py shell < scripts/create_superuser.py
python manage.py runserver 0.0.0.0:8001

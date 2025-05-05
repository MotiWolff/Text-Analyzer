#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations text_analyzer
python manage.py migrate text_analyzer
python manage.py migrate

# Collect static files
python manage.py collectstatic --no-input
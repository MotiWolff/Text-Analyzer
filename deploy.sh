#!/bin/bash

echo "Activating virtual environment..."
source venv/bin/activate

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Applying database migrations..."
python manage.py migrate

echo "Starting Gunicorn server..."
gunicorn cyberLibrary.wsgi:application --bind 0.0.0.0:8000 --workers 3 --access-logfile - --error-logfile - 
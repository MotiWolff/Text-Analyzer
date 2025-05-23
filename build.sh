#!/usr/bin/env bash
# exit on error
set -o errexit

echo "Starting build process..."

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt
pip install gunicorn

# Run migrations
echo "Running migrations..."
python manage.py makemigrations text_analyzer --verbosity 3
python manage.py migrate text_analyzer --verbosity 3
python manage.py migrate --verbosity 3

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --no-input

echo "Build process completed!"
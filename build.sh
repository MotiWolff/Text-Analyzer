#!/usr/bin/env bash
# exit on error
set -o errexit

echo "Starting build process..."

# Create data directory
echo "Creating data directory..."
mkdir -p data
chmod 777 data

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Run migrations
echo "Running migrations..."
python manage.py makemigrations text_analyzer --verbosity 3
python manage.py migrate text_analyzer --verbosity 3
python manage.py migrate --verbosity 3

# Verify migrations
echo "Verifying migrations..."
python manage.py showmigrations text_analyzer

# Force create table if it doesn't exist
echo "Ensuring table exists..."
python manage.py dbshell << EOF
CREATE TABLE IF NOT EXISTS text_analyzer_textanalysis (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(200) NOT NULL,
    content TEXT NOT NULL,
    created_at DATETIME NOT NULL,
    word_count INTEGER NOT NULL,
    sentence_count INTEGER NOT NULL,
    unique_words_count INTEGER NOT NULL,
    most_common_word VARCHAR(100) NOT NULL,
    most_common_word_count INTEGER NOT NULL,
    average_word_length FLOAT NOT NULL,
    longest_words JSON NOT NULL,
    frequency_words JSON NOT NULL,
    equal_length_sequences JSON NOT NULL
);
EOF

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --no-input

echo "Build process completed!"
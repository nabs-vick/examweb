#!/bin/bash
# Exit immediately if any command fails
set -e

# Apply database migrations
echo "Applying migrations..."
python manage.py migrate --no-input

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --no-input

# Start Gunicorn
echo "Starting server..."
gunicorn your_project_name.wsgi --bind 0.0.0.0:$PORT --workers 2
#!/bin/bash

# Activate virtual environment if you have one (optional)
source myenv/bin/activate

# Export Flask environment variables
export FLASK_APP=app.py
export FLASK_ENV=development  # Use "production" for production

# Run the Flask app
flask run

echo "Flask app started successfully."

#!/bin/bash

source .venv/bin/activate
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
echo "Successful completion of setup"
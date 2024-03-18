#!/bin/bash

if ! command -v virtualenv &> /dev/null; then
    echo "virtualenv is not installed. Installing..."
    pip install virtualenv
fi

virtualenv venv

source venv/bin/activate

pip install -r requirements.txt


python create_json_file.py

uvicorn fastapi_app:app --reload

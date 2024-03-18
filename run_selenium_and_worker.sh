#!/bin/bash

if ! command -v virtualenv &> /dev/null; then
    echo "virtualenv is not installed. Installing..."
    pip install virtualenv
fi

virtualenv venv

source venv/bin/activate

pip install -r requirements.txt

python parse_companies_names.py

celery -A tasks worker -Q companies_queue --loglevel=debug

python create_json_file.py

uvicorn app:fastapi_app --reload

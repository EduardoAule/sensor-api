#!/bin/bash
# flask settings
#export FLASK_APP=/some_path/my_flask_app.py
#export FLASK_DEBUG=0

#flask run --host=0.0.0.0 --port=80
python3 -m uvicorn main:app --host 0.0.0.0 --port 8000
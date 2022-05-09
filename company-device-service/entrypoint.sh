#!/bin/bash
# run any setup code
#./scripts/setup
# create the webserver
#gunicorn --worker-tmp-dir /dev/shm --config gunicorn.config.py app.api.main:app
gunicorn --worker-tmp-dir /dev/shm --config gunicorn.config.py app.api.main:app
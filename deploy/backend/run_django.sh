#!/bin/sh

# wait for PSQL server to start
sleep 5
cd src
gunicorn interview.wsgi:application --bind=0.0.0.0:8080 --workers=20 --timeout=300
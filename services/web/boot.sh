#!/bin/bash

# Error handling
#   standard_init_linux.go:219: exec user process caused: no such file or directory
#     This is an error caused by Windows. Open git bash and run doc2unix boot.sh to fix

echo Sleeping to wait for Postgres to wake up
# Ugly method to wait for Postgres to start
sleep 1

python manage.py runserver 0.0.0.0:8000
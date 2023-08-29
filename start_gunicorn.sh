#!/bin/bash

# Aktivieren Sie Ihre Python-Virtualenv
source /opt/www/django_netflix_clone/venv/bin/activate

# Setzen Sie die Umgebungsvariable SECRET_KEY
export SECRET_KEY=secret_key 

# Starten Sie Gunicorn mit dem Unix-Socket
/opt/www/django_netflix_clone/venv/bin/gunicorn django_netflix.wsgi:application --bind unix:/opt/www/django_netflix_clone/gunicorn.sock


#!/bin/bash

NAME="phil2flix"                                      # Name of the application
DJANGODIR=/opt/www/django_philflix                    # Django project directory
SOCKFILE=/opt/www/django_philflix/philflix/gunicorn.sock       # we will communicate using this unix socket
USER=iron-man                                        # the user to run as
GROUP=iron-man                                       # the group to run as
NUM_WORKERS=3                                        # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=philflix.settings       # which settings file should Django use
DJANGO_WSGI_MODULE=philflix.wsgi               # WSGI module name

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
source /opt/www/django_philflix/.SECRET_KEY
source /opt/www/django_philflix/venv/bin/activate

# Export for Gunicorn
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# # Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start Gunicorn
exec gunicorn $DJANGO_WSGI_MODULE:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
  --log-file=-

# philflix.wsgi:application --name phil2flix --workers 3 --user=iron --group=iron --bind=unix:/opt/www/django_philflix/philflix/gunicorn_phil2flix.sock --log-level=debug --log-file=-

# Aktivieren Sie Ihre Python-Virtualenv
#source /opt/www/django_philflix/venv/bin/activate
# source /opt/www/django_netflix_clone/venv/bin/activate
# source /opt/www/django_philflix/venv/bin/activate

# Setzen Sie die Umgebungsvariable SECRET_KEY
#export SECRET_KEY=secret_key 

# Starten Sie Gunicorn mit dem Unix-Socket
#exec /opt/www/django_philflix/venv/bin/gunicorn django_philflix.wsgi:application --bind unix:/opt/www/django_philflix/gunicorn.sock
# /opt/www/django_netflix_clone/venv/bin/gunicorn django_netflix.wsgi:application --bind unix:/opt/www/django_netflix_clone/gunicorn.sock
# /opt/www/django_philflix/venv/bin/gunicorn django_philflix.wsgi:application --bind unix:/opt/www/django_philflix/gunicorn.sock

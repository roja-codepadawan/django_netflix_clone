"""Gunicorn *development* config file"""
import os


# Django WSGI application path in pattern MODULE_NAME:VARIABLE_NAME
wsgi_app = "django_philflix.wsgi.application" # django_netflix.wsgi:application "project.wsgi:application"
# The granularity of Error log outputs
loglevel = "debug"
# The number of worker processes for handling requests
workers = 10
# The socket to bind
#bind = os.environ.get('GUNICORN_BIND', '0.0.0.0:8080')
bind = "0.0.0.0:8000" # 134.176.98.126:8000
# Restart workers when code changes (development only!)
reload = True
# Write access and error info to /var/log
accesslog = errorlog = "/var/log/gunicorn/dev.log"
# Redirect stdout/stderr to log file
capture_output = True
# PID file so you can easily fetch process ID
pidfile = "/var/run/gunicorn/dev.pid"
# Daemonize the Gunicorn process (detach & enter background)
daemon = True
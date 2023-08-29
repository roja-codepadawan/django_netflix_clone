. venv/bin/activate
pip install django-allauth
python -m pip install Pillow
python3 manage.py makemigrations       
python3 manage.py migrate --run-syncdb 

python manage.py makemigrations
python manage.py migrate
python manage.py migrate --run-syncdb

./manage.py schemamigration research --auto 
./manage.py schemamigration research --init
./manage.py migrate research


python3 manage.py createsuperuser
System check identified some issues:

WARNINGS:
core.CustomUser: (models.W042) Auto-created primary key used when not defining a primary key type, by default 'django.db.models.AutoField'.
	HINT: Configure the DEFAULT_AUTO_FIELD setting or the CoreConfig.default_auto_field attribute to point to a subclass of AutoField, e.g. 'django.db.models.BigAutoField'.
core.Movie: (models.W042) Auto-created primary key used when not defining a primary key type, by default 'django.db.models.AutoField'.
	HINT: Configure the DEFAULT_AUTO_FIELD setting or the CoreConfig.default_auto_field attribute to point to a subclass of AutoField, e.g. 'django.db.models.BigAutoField'.
core.Profile: (models.W042) Auto-created primary key used when not defining a primary key type, by default 'django.db.models.AutoField'.
	HINT: Configure the DEFAULT_AUTO_FIELD setting or the CoreConfig.default_auto_field attribute to point to a subclass of AutoField, e.g. 'django.db.models.BigAutoField'.
core.Video: (models.W042) Auto-created primary key used when not defining a primary key type, by default 'django.db.models.AutoField'.
	HINT: Configure the DEFAULT_AUTO_FIELD setting or the CoreConfig.default_auto_field attribute to point to a subclass of AutoField, e.g. 'django.db.models.BigAutoField'.
Username: django
Email address: django
Error: Enter a valid email address.
Email address: django@uni.de
Password: 
Password (again): 
This password is too common.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.



https://www.youtube.com/watch?v=gbyYXgiSgdM
https://stackoverflow.com/questions/25771755/django-operationalerror-no-such-table
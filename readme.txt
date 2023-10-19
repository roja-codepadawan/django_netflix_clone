. venv/bin/activate
pip install django-allauth
python -m pip install Pillow
python3 manage.py makemigrations       
python3 manage.py migrate --run-syncdb 

python manage.py makemigrations
python manage.py migrate
python manage.py migrate --run-syncdb
python manage.py collectstatic

python3 manage.py inspectdb
python manage.py flush


./manage.py schemamigration research --auto 
./manage.py schemamigration research --init
./manage.py migrate research


python3 manage.py createsuperuser
System check identified some issues:

sudo nginx -t
sudo systemctl restart nginx
sudo systemctl restart gunicorn
systemctl status gunicorn
/var/log/nginx/

ronrupp@fb07mac-u103804 ~ % scp -r iron-man@134.176.98.126/etc/nginx/sites-available/nginx_backup.zip /Users/ronrupp/Documents/Projects/Django/djangoBackup
cp: iron-man@134.176.98.126/etc/nginx/sites-available/nginx_backup.zip: No such file or directory
ronrupp@fb07mac-u103804 ~ % scp -r iron-man@134.176.98.126/etc/nginx/sites-available/nginx_backup.zip /Users/ronrupp/Documents/Projects/Django/djangoBackup
cp: iron-man@134.176.98.126/etc/nginx/sites-available/nginx_backup.zip: No such file or directory
ronrupp@fb07mac-u103804 ~ % scp -r iron-man@134.176.98.126:/etc/nginx/sites-available/nginx_backup.zip /Users/ronrupp/Documents/Projects/Django/djangoBackup
iron-man@134.176.98.126's password: 
nginx_backup.zip                                                                                                        100% 8892     4.1MB/s   00:00    
ronrupp@fb07mac-u103804 ~ % scp -r iron-man@134.176.98.126:/opt/www/django_netflix_clone.zip /Users/ronrupp/Documents/Projects/Django/djangoBackup
iron-man@134.176.98.126's password: 
django_netflix_clone.zip                                                                                                      100%  938MB  82.1MB/s   00:11    
ronrupp@fb07mac-u103804 ~ % 


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
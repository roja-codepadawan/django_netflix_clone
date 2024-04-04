"""
                  {{ project_name }}
Django settings for django_netflix project.

Generated by 'django-admin startproject' using Django 3.1.5.
For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/

Quick-start development settings - unsuitable for production
See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/
"""
import os
from pathlib import Path
from dotenv import load_dotenv
from django.utils.translation import gettext_lazy as _
import json

####################
#       CORE       #
####################

# load the environment variables from your .env file into your settings.py
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Pfad zur Datei mit dem Geheimschlüssel
secret_key_file = '/opt/www/django_philflix/.DJANGO_SECRET_KEY'

# Prüfe, ob die Datei vorhanden ist und lies den Geheimschlüssel
if os.path.exists(secret_key_file):
    with open(secret_key_file) as f:
        SECRET_KEY = f.read().strip()
else:
    # Falls die Datei nicht gefunden wird, erzeuge einen Fehler
    raise FileNotFoundError(f"Secret key file '{secret_key_file}' not found")

# Wenn die Umgebungsvariable nicht gefunden wird, wirf einen Fehler
if not SECRET_KEY:
    raise RuntimeError("Could not find a SECRET_KEY in environment")

# Lade die sensiblen Informationen aus credentials.json
with open('credentials.json') as f:
    credentials = json.load(f)

# Setze das E-Mail-Passwort in den Einstellungen
EMAIL_USER = credentials.get('EMAIL_USER')
EMAIL_PASSWORD = credentials.get('EMAIL_PASSWORD')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


# Hosts/domain names that are valid for this site.
# "*" matches anything, ".example.com" matches example.com and all subdomains
ALLOWED_HOSTS = [
    'localhost',
	'134.176.98.126',
	'*.fb07dida-jarvis.didaktik.physik.uni-giessen.de',
    '.phil2flix.uni-giessen.de',
    '*.uni-giessen.de'
]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'core',
    # 'philflix',

    # thir party apps
    'allauth',
    'allauth.account',
    # 'allauth.socialaccount',
    
    # debug toolbar
    # 'debug_toolbar',
]


##############
# MIDDLEWARE #
##############
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    # debug toolbar
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
]

#######################
# SECURITY MIDDLEWARE #
#######################
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_CROSS_ORIGIN_OPENER_POLICY = "same-origin"
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_HSTS_SECONDS = 31536000
SECURE_REDIRECT_EXEMPT = []
SECURE_REFERRER_POLICY = "same-origin"
SECURE_SSL_HOST = None
SECURE_SSL_REDIRECT = True

# Add the following line to allow serving static files over HTTPS
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
)


MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'philflix.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # BASE_DIR/'templates'
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
                'django.template.context_processors.static', # ----
		        'django.template.context_processors.media', # ---
            ],
            # 'loaders': [
            #     'django.template.loaders.filesystem.Loader',
            #     'django.template.loaders.app_directories.Loader',
            # ],
        },
    },
]


WSGI_APPLICATION = 'philflix.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'mydatabase',
#         'USER': 'mydatabaseuser',
#         'PASSWORD': 'mypassword',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.environ.get('DB_NAME'),
#         'USER': os.environ.get('DB_USER'),
#         'PASSWORD': os.environ.get('DB_PASSWORD'),
#         'HOST': os.environ.get('DB_HOST', 'localhost'),
#         'PORT': os.environ.get('DB_PORT', '5432'),
#     }
# }

# Default primary key field type.
DEFAULT_AUTO_FIELD = "django.db.models.AutoField" # 'django.db.models.BigAutoField'


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Standardmäßige Sprache
LANGUAGE_CODE = 'de-DE' # 'en-us'

# Local time zone for this installation. All choices can be found here:
# https://en.wikipedia.org/wiki/List_of_tz_zones_by_name (although not all
# systems may support all possibilities). When USE_TZ is True, this is
# interpreted as the default user time zone.
TIME_ZONE = "Europe/Berlin"

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/
LANGUAGES = [
    ("de", _("German")),
    ("en", _("English")),
]
USE_I18N = True
# Pfade zu den Übersetzungsdateien
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

USE_L10N = True

USE_TZ = True

# Default charset to use for all HttpResponse objects, if a MIME type isn't
# manually specified. It's used to construct the Content-Type header.
DEFAULT_CHARSET = "utf-8"

###############
# STATICFILES #
###############
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

# Set the directory where static files will be collected for deployment
# STATIC_ROOT = BASE_DIR/'static_root' 
STATIC_ROOT=BASE_DIR/'static' 
# STATIC_ROOT = rel('..', 'static')
# STATIC_ROOT = '/opt/www/django_philflix/static_root/'
STATIC_URL='/static/'

# Media files (uploads)
# MEDIA_ROOT='/mnt/share/media' 
MEDIA_ROOT=BASE_DIR/'media'
MEDIA_URL='/media/'

# A list of locations of additional static files
# Set the directory where your project-specific static files are located
STATICFILES_DIRS=[
    # BASE_DIR/'static',
    # BASE_DIR/'static_root',
]
# The default file storage backend used during the build process
# STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"
# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

FILE_UPLOAD_HANDLERS = [
    "django.core.files.uploadhandler.MemoryFileUploadHandler",
    "django.core.files.uploadhandler.TemporaryFileUploadHandler",
]
FILE_UPLOAD_TIMEOUT = 600  # Timeout in Sekunden (10 Minuten)
DATA_UPLOAD_MAX_MEMORY_SIZE = 16106127360  # 15 GB in Bytes

##################
# AUTHENTICATION #
##################
AUTH_USER_MODEL='core.CustomUser'

AUTHENTICATION_BACKENDS = [

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
  
]


ACCOUNT_AUTHENTICATION_METHOD='email'
ACCOUNT_EMAIL_REQUIRED=True
ACCOUNT_UNIQUE_EMAIL=True
EMAIL_CONFIRMATION_SINGUP=True
#Account email verification: This option can be used to set whether an email verification is necessary for a user to log in after he registers an account. You can use ‘mandatory’ to block a user from logging in until the email gets verified. You can set options for sending the email but allowing the user to log in without an email. You can also set none to send no verification email. (Not Recommended)
ACCOUNT_EMAIL_VERIFICATION='mandatory'   
# ACCOUNT_EMAIL_VERIFICATION='none'
#Email confirmation expiry: Sets the number of days within which an account should be activated.
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS=7
ACCOUNT_USERNAME_REQUIRED=False


#####################
# Emailing settings #
#####################
# SMTP backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# Console backend
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

EMAIL_HOST = 'smtp.uni-giessen.de'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'ron.rupp@sowi.uni-giessen.de'
EMAIL_HOST_USER = EMAIL_USER    # Verwende die geladene Einstellung
EMAIL_HOST_PASSWORD = EMAIL_PASSWORD    # Verwende die geladene Einstellung

# Email address that error messages come from.
SERVER_EMAIL = "phil2flix@uni-giessen.de"

# Default email address to use for various automated correspondence from the site managers.
DEFAULT_FROM_EMAIL = "phil2flix@uni-giessen.de"

# Subject-line prefix for email messages send with django.core.mail.mail_admins
# or ...mail_managers.  Make sure to include the trailing space.
EMAIL_SUBJECT_PREFIX = "[PHIL II FLIX] "

LOGIN_REDIRECT_URL='/'

SITE_ID=1


#####################
# ERROR LOG         #
#####################
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '\n----------\n{levelname} {asctime} {module} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',  # Change this
            'class': 'logging.FileHandler',
            'filename': '/opt/www/django_philflix/debug.log',
            'formatter': 'verbose',
        },
    },
    'root': {
        'handlers': ['file'],
        'level': 'INFO',  # And this
    },
}

# #####################
# # DEBUG TOOLBAR     #
# #####################
# DEBUG_TOOLBAR_PANELS = [
#     'debug_toolbar.panels.versions.VersionsPanel',
#     'debug_toolbar.panels.timer.TimerPanel',
#     'debug_toolbar.panels.settings.SettingsPanel',
#     'debug_toolbar.panels.headers.HeadersPanel',
#     'debug_toolbar.panels.request.RequestPanel',
#     'debug_toolbar.panels.sql.SQLPanel',
#     'debug_toolbar.panels.staticfiles.StaticFilesPanel',
#     'debug_toolbar.panels.templates.TemplatesPanel',
#     'debug_toolbar.panels.cache.CachePanel',
#     'debug_toolbar.panels.signals.SignalsPanel',
#     'debug_toolbar.panels.logging.LoggingPanel',
#     'debug_toolbar.panels.redirects.RedirectsPanel',
# ]

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
from django.utils.translation import gettext_lazy as _
import json




####################
#       CORE       #
####################


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")
try:
    SECRET_KEY = os.environ["SECRET_KEY"]
except KeyError as e:
    raise RuntimeError("Could not find a SECRET_KEY in environment") from e


# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = os.getenv("DEBUG") == False  # Convert to boolean if needed False
DEBUG = False # True


# Lade die sensiblen Informationen aus credentials.json
with open('credentials.json') as f:
    credentials = json.load(f)

# Setze das E-Mail-Passwort in den Einstellungen
EMAIL_USER = credentials.get('EMAIL_USER')
EMAIL_PASSWORD = credentials.get('EMAIL_PASSWORD')


# Hosts/domain names that are valid for this site.
# "*" matches anything, ".example.com" matches example.com and all subdomains
ALLOWED_HOSTS = [
    'localhost',
	'134.176.98.126',
	'.fb07dida-jarvis.didaktik.physik.uni-giessen.de'
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

    # thir party apps
    'allauth',
    'allauth.account',
    # 'allauth.socialaccount',
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
]

#######################
# SECURITY MIDDLEWARE #
#######################
# SECURE_CONTENT_TYPE_NOSNIFF = True
# SECURE_CROSS_ORIGIN_OPENER_POLICY = "same-origin"
# SECURE_HSTS_INCLUDE_SUBDOMAINS = False
# SECURE_HSTS_PRELOAD = False
# SECURE_HSTS_SECONDS = 0
# SECURE_REDIRECT_EXEMPT = []
# SECURE_REFERRER_POLICY = "same-origin"
# SECURE_SSL_HOST = None
# SECURE_SSL_REDIRECT = False

ROOT_URLCONF = 'django_netflix.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR/'templates'
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
        },
    },
]

WSGI_APPLICATION = 'django_netflix.wsgi.application'



# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGES = [
    ("de", _("German")),
    ("en", _("English")),
]

# Standardmäßige Sprache
LANGUAGE_CODE = 'de-DE' # 'en-us'

# Local time zone for this installation. All choices can be found here:
# https://en.wikipedia.org/wiki/List_of_tz_zones_by_name (although not all
# systems may support all possibilities). When USE_TZ is True, this is
# interpreted as the default user time zone.
TIME_ZONE = "Europe/Berlin"

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
STATIC_ROOT = BASE_DIR/'static_root' 
STATIC_URL = '/static/'

# Media files (uploads)
MEDIA_ROOT='/mnt/share/media'   # MEDIA_ROOT=BASE_DIR/'media'
MEDIA_URL='/media/'


# A list of locations of additional static files
# Set the directory where your project-specific static files are located
STATICFILES_DIRS=[
    BASE_DIR/'static',
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

# Auth stting
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
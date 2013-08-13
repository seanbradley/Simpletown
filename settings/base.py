# DJANGO BASE SETTINGS

import os, sys
from os import environ
from os.path import basename
from unipath import Path


########## PATH CONFIGURATION
PROJECT_DIR = Path(__file__).ancestor(2)
MEDIA_ROOT = PROJECT_DIR.child("media")
STATIC_ROOT = PROJECT_DIR.child("static")
STATICFILES_DIRS = (
    PROJECT_DIR.child("styles"),
)
TEMPLATE_DIRS = (
    PROJECT_DIR.child("templates"),
)
ROOT_URLCONF = 'urls'

# Site name...
SITE_NAME = basename(PROJECT_DIR)
########## END PATH CONFIGURATION


########## EXCEPTION HANDLING
# Normally you should not import ANYTHING from Django directly into your
# settings, but ImproperlyConfigured is an exception.
from django.core.exceptions import ImproperlyConfigured

def get_env_setting(setting):
    """ Get the environment setting or return exception """
    try:
        return environ[setting]
    except KeyError:
        error_msg = "Set the %s env variable" % setting
        raise ImproperlyConfigured(error_msg)
########## END EXCEPTION HANDLING


########## MEDIA CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'

#ADMIN_MEDIA_PREFIX = ""

########## END MEDIA CONFIGURATION


########## STATIC FILE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)
########## END STATIC FILE CONFIGURATION


########## TEMPLATE CONFIGURATION
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#    'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth'
)
########## END TEMPLATE CONFIGURATION


########## DATABASE CONFIGURATION
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ubuntu',       # Or path to database file if using sqlite3
        'USER': 'ubuntu',       # Change this in the Postgres shell
        'PASSWORD': 'ubuntu',   # Obviously, use a better password or environ variable for production
        'HOST': 'localhost',    # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP
        'PORT': '',             # Set to empty string for default.
    }
}
########## END DATABASE CONFIGURATION


########## MIDDLEWARE CONFIGURATION
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
########## END MIDDLEWARE CONFIGURATION


########## APPS CONFIGURATION
WSGI_APPLICATION = 'wsgi.application'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'south',
    'registration',
    'cities'
    # Some add'l useful apps you might want to install if using SIMPLETOWN'S FAST LANE AMI
    #'django.contrib.admindocs',
    #'django-extensions', #to use, just uncomment this line
    #'djcelery'  #to use, uncomment lines in CELERY CONFIGURATION below
    #'kombu.transport.django' #to use, uncomment lines in CELERY CONFIGURATION below
)
########## END APPS CONFIGURATION


########## CELERY CONFIGURATION
#import djcelery
#djcelery.setup.loader()
#BROKER_URL = "django://"  #use celeryd -l info
########## END CELERY CONFIGURATION


########## ADMNISTRATORS
ADMINS = (
    ('Your Name', 'you@yourdomain.com'),
)

MANAGERS = ADMINS
########## END ADMNISTRATORS


########## USER REGISTRATION / ACTIVATION CONFIGURATION
ACCOUNT_ACTIVATION_DAYS = 7
DEFAULT_FROM_EMAIL = 'webmaster@localhost'
LOGIN_REDIRECT_URL = '/'
########## END USER REGISTRATION / ACTIVATION CONFIGURATION


########## EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-password
EMAIL_HOST_PASSWORD = environ.get('EMAIL_HOST_PASSWORD', '')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-user
EMAIL_HOST_USER = environ.get('EMAIL_HOST_USER', '')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = '[%s] ' % SITE_NAME

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-use-tls
EMAIL_USE_TLS = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#server-email
SERVER_EMAIL = EMAIL_HOST_USER
########## END EMAIL CONFIGURATION


########## MISC SETTINGS
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# And: http://drumcoder.co.uk/blog/2010/nov/12/apache-environment-variables-and-mod_wsgi/
SECRET_KEY = os.environ['SECRET_KEY']

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name although not all
# choices may be available on all operating systems. On Unix systems, a value
# of None will cause Django to use the same timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Los_Angeles'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html.
LANGUAGE_CODE = 'en-us'

# The ID, as an integer, of the current site in the django_site database table.
# This is used so that application data can hook into specific site(s) and a
# single database can manage content for multiple sites.
SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True
########## END MISC SETTINGS


########## DEBUG CONFIGURATION
DEBUG =  bool(os.environ.get('DEBUG', False))
########## END DEBUG CONFIGURATION


########## LOG CONFIGURATION
# A sample logging configuration. The only tangible logging performed by
# this configuration is to send an email to the site admins on every
# HTTP 500 error when DEBUG=False.

# See http://docs.djangoproject.com/en/dev/topics/logging for more details
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
########## END LOG CONFIGURATION
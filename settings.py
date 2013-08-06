# DJANGO SETTINGS

import os, sys
from os import environ
from os.path import basename
from sys import path
from unipath import Path


########## PATH CONFIGURATION
PROJECT_DIR = Path(__file__).ancestor(1)
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

# Add our project to our pythonpath, this way we don't need to type our
# project name in our dotted import paths...
path.append(PROJECT_DIR)
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
    #'registration_defaults',  #to use, may need to uncomment REGISTRATION_TEMPLATE_DIR below
    #'debug_toolbar', #to use, uncomment appropriate lines in DEBUG CONFIGURATION below
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

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host
EMAIL_HOST = environ.get('EMAIL_HOST', 'smtp.gmail.com')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-password
EMAIL_HOST_PASSWORD = environ.get('EMAIL_HOST_PASSWORD', '')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-user
EMAIL_HOST_USER = environ.get('EMAIL_HOST_USER', '')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-port
EMAIL_PORT = environ.get('EMAIL_PORT', 587)

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
SECRET_KEY = environ.get('SECRET_KEY')

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
# Include in ALLOWED_HOSTS the IP returned from curl http://169.254.169.254/latest/meta-data/public-ipv4
# Remove "*" to garner the security benefit of this setting
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "*"]

TIME_ZONE = 'America/Los_Angeles'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True
########## END MISC SETTINGS


########## DEBUG CONFIGURATION
DEBUG =  bool(os.environ.get('DEBUG', False))
#TEMPLATE_DEBUG = DEBUG

'''
# Django-Debug-Toolbar settings...
# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TEMPLATE_CONTEXT': True,
}
'''
########## END DEBUG CONFIGURATION


########## LOG CONFIGURATION
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
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
# Django settings for sb_biz project.
import os, sys
from os.path import abspath, basename, dirname, join, normpath
from sys import path

# Secret key, e-mail password, etc. require setting environment variables
# to avoid making these visible in repo and elsewhere; hence, import environ...
from os import environ

# Normally you should not import ANYTHING from Django directly into your 
# settings, but ImproperlyConfigured is an exception.
from django.core.exceptions import ImproperlyConfigured

# Importing everything implicitly is bad and goes against the Zen is Python.
# But my laziness and desire not to redraft 15 templates is perhaps more
# Zen than you know. Now, if only I'd adopt class-based views, then I'd 
# be a Zen master... See https://github.com/yourcelf/django-registration-defaults
#from registration_defaults.settings import *

'''
def get_env_setting(setting):
    """ Get the environment setting or return exception """
    try:
        return environ[setting]
    except KeyError:
        error_msg = "Set the %s env variable" % setting
        raise ImproperlyConfigured(error_msg)
'''

ADMINS = (
    ('Sean Bradley', 'sean@blogblimp.com'),
)

MANAGERS = ADMINS

ROOT_URLCONF = 'urls'


########## PATH CONFIGURATION
# Absolute filesystem path to the Django project directory...
DJANGO_ROOT = dirname(abspath(__file__))   #/srv/django/sb_biz/sb_biz

# Absolute filesystem path to the top-level project folder...
# One level higher than typical two_scoops directory structure.
SITE_ROOT = dirname(DJANGO_ROOT)

# Site name...
SITE_NAME = basename(DJANGO_ROOT)

# Add our project to our pythonpath, this way we don't need to type our project
# name in our dotted import paths...
path.append(DJANGO_ROOT)
########## END PATH CONFIGURATION


########## STATIC FILE CONFIGURATION
# All style related docs are in here...

# Django can get rather nuanced with the way it deals with static files.
# Particularly, it's careful with regard to namespacing of static files.
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
# And: https://docs.djangoproject.com/en/dev/howto/static-files/
# Typically, "manage.py collectstatic" gathers all static files included
# in STATICFILES_DIRS into the STATIC_ROOT directory...  Also, typically,
# STATIC_ROOT is called "assets".  But, for ease of this deployment, all
# the static and style-related files (except for admin styles) are already
# in one directory. So, we're pointing STATIC_ROOT directly to that directory.
STATIC_ROOT = normpath(join(SITE_ROOT, 'static/site-styles'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/static/'

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = (
    #normpath(join(SITE_ROOT, 'static')),
)

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

#ADMIN_MEDIA_PREFIX = ""

########## END STATIC FILE CONFIGURATION


########## MEDIA CONFIGURATION
# I usually reserve "media" directories for files uploaded by users,
# and let static assets live specifically in directories named "static".
# Django has its own ideas about that, however...

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = normpath(join(SITE_ROOT, 'media'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'
########## END MEDIA CONFIGURATION


########## TEMPLATE CONFIGURATION
# The order of things here is important.
TEMPLATE_DIRS = (
    #"/srv/django/sb_biz/templates"
    normpath(join(SITE_ROOT, 'templates')),
    #REGISTRATION_TEMPLATE_DIR,
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)
########## END TEMPLATE CONFIGURATION


########## USER REGISTRATION / ACTIVATION CONFIGURATION
ACCOUNT_ACTIVATION_DAYS = 7
DEFAULT_FROM_EMAIL = 'webmaster@localhost'
LOGIN_REDIRECT_URL = '/'
########## END USER REGISTRATION / ACTIVATION CONFIGURATION


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
WSGI_APPLICATION = 'sb_biz.wsgi.application'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    #'registration_defaults',
    #'django.contrib.admindocs',
    #'debug_toolbar',
    #'south',
    'registration',
    'cities'
)
########## END APPS CONFIGURATION


########## DATABASE CONFIGURATION
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ubuntu',       # Or path to database file if using sqlite3.
        'USER': 'ubuntu',
        'PASSWORD': 'ubuntu',   # Obviously, use a better password or environ variable for production...
        'HOST': 'localhost',    # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',             # Set to empty string for default.
    }
}
########## END DATABASE CONFIGURATION


########## EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host
EMAIL_HOST = environ.get('EMAIL_HOST', 'smtp.gmail.com')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-password
EMAIL_HOST_PASSWORD = environ.get('EMAIL_HOST_PASSWORD', '')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-user
EMAIL_HOST_USER = environ.get('EMAIL_HOST_USER', 'sean@blogblimp.com')

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
ALLOWED_HOSTS = ["localhost", "23.21.214.134", "ec2-184-72-94-22.compute-1.amazonaws.com"]

TIME_ZONE = 'America/Los_Angeles'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True
########## END MISC SETTINGS


########## DEBUG CONFIGURATION
DEBUG = True #set this to false in production; make sure you have valid ALLOWED_HOSTS
TEMPLATE_DEBUG = DEBUG #comment out in production

#Django-Debug-Toolbar (see "INSTALLED_APPS")
'''
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

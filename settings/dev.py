# DJANGO DEVELOPMENT SETTINGS

from .base import *

INTERNAL_IPS = ('127.0.0.1',)

INSTALLED_APPS += (
    'debug_toolbar',
)


########## ADD'L DEBUG CONFIGURATION
TEMPLATE_DEBUG = DEBUG

# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TEMPLATE_CONTEXT': True,
}
########## END ADD'L DEBUG CONFIGURATION


########## ADD'L EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host
EMAIL_HOST = "localhost"

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-port
EMAIL_PORT = 1025
########## END ADD'L EMAIL CONFIGURATION
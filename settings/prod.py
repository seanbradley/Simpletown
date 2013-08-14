# DJANGO PRODUCTION SETTINGS

import requests
from .base import *

########## ADD'L MISC SETTINGS
from requests.exceptions import ConnectionError

url = "http://169.254.169.254/latest/meta-data/public-ipv4"
try:
    r = requests.get(url)
    instance_ip = r.text
    ALLOWED_HOSTS += [instance_ip]
except ConnectionError:
    error_msg = "You can only run production settings on an AWS EC2 instance"
    raise ImproperlyConfigured(error_msg)
########## END ADD'L MISC SETTINGS

########## ADD'L EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host
EMAIL_HOST = environ.get('EMAIL_HOST', 'smtp.gmail.com')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-port
EMAIL_PORT = environ.get('EMAIL_PORT', 587)
########## END ADD'L EMAIL CONFIGURATION

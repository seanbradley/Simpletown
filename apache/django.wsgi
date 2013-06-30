import os, sys
sys.path.append('/srv/django/sb_biz')
sys.path.append('srv/django')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sb_biz.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

#import django.core.handlers.wsgi
#application = django.core.handlers.wsgi.WSGIHandler()

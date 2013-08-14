import os, sys, pprint
#import monitor

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.prod")

# django site location
sys.path.append('srv/django')
sys.path.append('/srv/django/sb_biz')

# django core location
sys.path.append('/home/ubuntu/.virtualenvs/sb_biz/lib/python2.7/site-packages/django/')
sys.path.insert(0, os.path.join(os.path.abspath(os.path.dirname(__file__)),'..'))

from django.core.wsgi import get_wsgi_application
_application = get_wsgi_application()

# pull in an env var set in apache config
def application(environ, start_response):
  os.environ['SECRET_KEY'] = environ['SECRET_KEY']
  return _application(environ, start_response)

# monitor code changes
#monitor.start(interval=1.0)
#monitor.track(os.path.join(os.path.dirname(__file__), '..'))

# logging middleware
class LoggingMiddleware:

    def __init__(self, application):
        self.__application = application

    def __call__(self, environ, start_response):
        errors = environ['wsgi.errors']
        pprint.pprint(('REQUEST', environ), stream=errors)

        def _start_response(status, headers, *args):
            pprint.pprint(('RESPONSE', status, headers), stream=errors)
            return start_response(status, headers, *args)

        return self.__application(environ, _start_response)

application = LoggingMiddleware(application)

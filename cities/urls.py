from django.conf.urls import patterns, url

from cities.views import view_one

urlpatterns = patterns('',
    #url(r'^view_one/', ViewOne.as_view())
    url(r'^view_one/', 'view_one'),        
    #url(r'^view_two/', ViewTwo.as_view()),
)

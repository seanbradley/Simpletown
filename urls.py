from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

import registration
from main import views
from cities import views


urlpatterns = patterns('',

    ###### index #####
    url(r'^$', 'main.views.index'),
    
    ##### cities #####
    url(r'^view_one', 'cities.views.view_one'),

    ##### registration #####
    url(r'^accounts/', include('registration.urls')),

    ##### admin #####
    url(r'^admin/', include(admin.site.urls)),
    
)

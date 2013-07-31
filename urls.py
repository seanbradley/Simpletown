from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

import registration
from main import views
from cities.views import view_one, view_two


urlpatterns = patterns('',

    ###### index #####
    url(r'^$', 'main.views.index'),

    ##### cities #####
    url(r'^view_one', view_one),
    url(r'^view_two', view_two),

    ##### registration #####
    url(r'^accounts/', include('registration.urls')),

    ##### admin #####
    url(r'^admin/', include(admin.site.urls)),

)

from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

import registration
from main import views
from cars import views
from cities.views import view_one, view_two
#from cars.views import CarListView

urlpatterns = patterns('',

    ###### index #####
    url(r'^$', 'main.views.index'),

    ##### cities #####
    url(r'^view_one', view_one),
    url(r'^view_two', view_two),

    ##### cars #####
    url(r'^cars/', include('cars.urls')),

    ##### registration #####
    url(r'^accounts/', include('registration.urls')),

    ##### admin #####
    url(r'^admin/', include(admin.site.urls)),

)

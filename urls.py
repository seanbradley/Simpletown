from django.conf.urls import patterns, include, url
#from django.views.generic.simple import direct_to_template
from django.contrib import admin
from sb_biz import views
from cities import views
admin.autodiscover()


urlpatterns = patterns('',

    ###### home page #####
    #url(r'^$', direct_to_template, { 'template': 'index.html' }, 'index'),
    url(r'^$', IndexView.as_view()),
    
    ##### view one #####
    url(r'^view_one', 'cities.views.view_one'),

    ##### login, logout, etc #####
    url(r'^accounts/', include('registration.urls')),
    #url(r'^accounts/login/$', 'django.contrib.auth.views.login'),

    ##### admin dashboard #####
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
    ##### urls for CBVs #####
    #url(r'^view_one/', ViewOne.as_view()),    
    #url(r'^view_two/', ViewTwo.as_view()),
    
)

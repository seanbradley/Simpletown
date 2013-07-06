from django.conf.urls import patterns, include, url
#from django.views.generic.simple import direct_to_template
from django.contrib import admin
from sb_biz import views
from cities import views
admin.autodiscover()
 
urlpatterns = patterns('',
    (r'^admin/(.*)', admin.site.root),
    (r'^accounts/', include('registration.urls')),
    (r'^$', direct_to_template, 
            { 'template': 'index.html' }, 'index'),
)


urlpatterns = patterns('',

    #url(r'^$', direct_to_template, { 'template': 'index.html' }, 'index'),
    url(r'^$', IndexView.as_view()),
    
    url(r'^view_one', 'cities.views.view_one'),

    url(r'^accounts/', include('registration.urls')),
    #url(r'^accounts/login/$', 'django.contrib.auth.views.login'),

    url(r'^admin/', include(admin.site.urls)),
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
    #url(r'^view_one/', ViewOne.as_view()),    
    #url(r'^view_two/', ViewTwo.as_view()),
    
)

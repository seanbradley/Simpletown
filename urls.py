from django.conf.urls import patterns, include, url
from django.contrib import admin
from sb_biz.views import IndexView
from cities.views import ViewOne, ViewTwo
admin.autodiscover()


urlpatterns = patterns('',

    url(r'^$', IndexView.as_view()),
    url(r'^view_one/', ViewOne.as_view()),    
    url(r'^view_two/', ViewTwo.as_view()),
        
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
)

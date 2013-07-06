from django.conf.urls import patterns, include, url
from django.contrib import admin
from sb_biz.views import IndexView
from cities import views

#from cities.views import view_one #, view_two #ViewOne, ViewTwo
admin.autodiscover()


urlpatterns = patterns('',

    url(r'^$', IndexView.as_view()),
    url(r'^view_one', 'cities.views.view_one'),
        
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
  
    #url(r'^view_one/', ViewOne.as_view()),    
    #url(r'^view_two/', ViewTwo.as_view()),
    
)

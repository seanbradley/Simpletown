from django.conf.urls import patterns, url

from cities import views

urlpatterns = patterns('',
    url(r'^cities/view_one$', views.view_one, name='view_one')
    url(r'^cities/view_two$', views.view_two, name='view_two')
)

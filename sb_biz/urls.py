from django.conf.urls import patterns, include, url
from django.contrib import admin
from sb_biz.views import IndexView


urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='home'),
)

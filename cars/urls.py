from django.conf.urls import patterns, url
from .views import dmv #, results #or CarListView

urlpatterns = patterns('',
    url(r'^dmv', 'cars.views.dmv'),
    #url(r'^results', 'cars.views.results'),
    #url(
    #    regex=r"^dmv/$",
    #    view=CarListView.as_view(),
    #    name="dmv"
    #),
)

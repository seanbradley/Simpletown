from django.conf.urls import patterns, url
from .views import dmv #, results #or CarListView

urlpatterns = patterns('',
    url(r'^dmv', 'cars.views.dmv'),

    # use the following for a class-based view...
    #url(
    #    regex=r"^dmv/$",
    #    view=CarListView.as_view(),
    #    name="dmv"
    #),

)

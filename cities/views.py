import re, requests, json
#from itertools import compress
#from operator import itemgetter, attrgetter

from django.views.generic import ListView
from django.views.generic.base import View, TemplateView, TemplateResponse
from django.views.generic.detail import DetailView
from django.template import loader, RequestContext
from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.http import HttpResponseRedirect

from cities.models import City
from cities.forms import CityForm
#from cities.tasks import taskname

def filter_one(messyData):

    for x in messyData:

        del x["description"], x["feat_class"], x["feature_id"], x["fips_class"], x["fips_county_cd"], x["full_county_name"], x["link_title"], x["url"], x["state_abbreviation"]

    return messyData


@login_required
@cache_page(3600) # Cache view result for one hour
def view_one(request):

    geo_data = []

    states = [
    "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
    "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
    "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
    "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
    "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"
    ]

    for state in states:

        url = "http://api.sba.gov/geodata/city_links_for_state_of/" + state + ".json"

        r = requests.get(url)

        data = r.json()

        # get rid of lots of extra params
        clean_data = filter_one(data)

        # append our geo_data list with one state
        geo_data.append(clean_data)

    # return all states...and mop up some bits and pieces of ancillary jive
    all_geo_data = str(geo_data).replace(',', '\n').replace('u\'', '\'').replace('\'', '').replace('[', '').replace(']', '').replace('{', '').replace('}', '\n')

    context = {'all_geo_data': all_geo_data}

    return render_to_response(
    'cities/view_one.html',
    RequestContext(request, context)
    )



@login_required
def view_two(request):

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            data = form.data['county_name']
            results = City.objects.filter(county_name = data)
            context = {'results': results}
            return render_to_response(
            'cities/results.html',
            RequestContext(request, context)
            )
    else:
        form = CityForm()
        context = {'form': form}
    return render_to_response(
    'cities/view_two.html',
    RequestContext(request, context)
    )
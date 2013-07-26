import re, requests, json
from itertools import compress
#from operator import itemgetter, attrgetter

from django.views.generic.base import View, TemplateView, TemplateResponse
from django.template import loader, RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

from cities.models import City
  
                      
def filter_one(messyData):
    
    for x in messyData:
        
        del x["description"], x["feat_class"], x["feature_id"], x["fips_class"], x["fips_county_cd"], x["full_county_name"], x["link_title"], x["url"], x["state_abbreviation"]
                        
    return messyData
    

@login_required
def view_one(self):
    
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
        
    context = { 'all_geo_data': all_geo_data }
    
    return render_to_response('cities/view_one.html', context)
    
    
    
@login_required
def view_two(self):
    
    cities = City.objects.all()
    
    context = {'cities': cities}
    
    return render_to_response('cities/view_two.html', context)


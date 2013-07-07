import re, requests, json
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

from cities.models import City
  
                      
def filter_one(data):
    
    for x in data:
        
        del x["description"], x["feat_class"], x["feature_id"], x["fips_class"], x["fips_county_cd"], x["full_county_name"], x["link_title"], x["url"], x["state_abbreviation"]
                        
    return data
    

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
        
    # return all states...and mop up some bits and pieces of ancillary jsonic jive
    all_geo_data = str(geo_data).replace(',', '\n').replace('u\'', '\'').replace('\'', '').replace('[', '').replace(']', '').replace('{', '').replace('}', '\n')
        
    context = { 'all_geo_data': all_geo_data }
    
    return render_to_response('cities/view_one.html', context)
    

'''
# See http://pydanny.com/the-easy-form-views-pattern-controversy.html
# vs. http://pydanny.com/core-concepts-django-modelforms.html
@login_required+
def view_two(request, template_name="cities/cities_form.html"):

    form = Cities(request.POST or None)
    if form.is_valid():
        do_x() # custom logic here
        return redirect('index')
    return render(request, template_name, {'form': form})
'''

import re, requests, json
from itertools import compress
#from operator import itemgetter, attrgetter

from django.views.generic.base import TemplateView
from django.template import loader, RequestContext

from cities.models import City
      
        
class ViewOne(TemplateView):
    
    '''
    The SB biz administration's api returns a full set of data like so:
    
    {"county_name":"Mobile","description":null,"feat_class":"Populated Place","feature_id":"256","fips_class":"C1","fips_county_cd":"97","full_county_name":"Mobile County","link_title":null,"url":"http:\/\/townofdauphinisland.org\/","name":"Dauphin Island","primary_latitude":"30.25","primary_longitude":"-88.1","state_abbreviation":"AL","state_name":"Alabama"},
    '''
        
    template_name = "cities/view_one.html"
    
    def get_json(self):
    
        rawData = []
        
        states = [
        "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
        "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
        "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
        "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
        "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"
        ]
    
        estados = states
                    
        #while
        
        for state in range(len(estados)):
                
                url = "http://api.sba.gov/geodata/city_links_for_state_of/" + estados[state] + ".json"
                estados.pop(0)

                r = requests.get(url)
                data = r.json()
                rawData.append(data)
                
                # rawData is a list within a list
                # get a list of data for one state
                messyData = rawData[0]
                
                # get rid of lots of extra params
                cleanData = self.filterTwo(messyData)
                
                # get rid of odds and ends
                return str(cleanData).replace(',', '\n').replace('u\'', '\'').replace('\'', '').replace('[', '').replace(']', '').translate(None, '{}')
            
        
    def filterOne(self, listData):
        columnarData = re.sub(',', '\n', listData)
        return columnarData
        
        
    def filterTwo(self, moreListData):
        # if moreListData is a list, do this...
        #if isinstance(moreListData, list):
        #    selectors = [1,0,0,0,0,0,0,1,1,1,0,0,0,0]
        #    lessData = compress(moreListData, selectors)
        #    return lessData
        # else it's probably a "list of dictionaries", so do this...
        # see: http://www.developer.nokia.com/Community/Wiki/Archived:List_of_Dictionaries_in_Python
        # and: http://wiki.python.org/moin/SortingListsOfDictionaries
        #else:
        for x in moreListData:
            del x["description"], x["feat_class"], x["feature_id"], x["fips_class"], x["fips_county_cd"], x["full_county_name"], x["link_title"], x["url"], x["state_abbreviation"]
        return moreListData
                
                
    def get_context_data(self):
        all_geo_data = self.get_json()
        return {
            "all_geo_data" : all_geo_data
        }
        
        
class ViewTwo(TemplateView):
 
    template_name = "cities/view_two.html"

    #list_by_county = []
    
    def get_context_data(self):
        return {
            #'list_by_county': list_by_county
        }


'''
def my_view_function(request, template='my_template.html'):
    context = {'favorite_color': settings.FAVORITE_COLOR}
    return render_to_response(template, context)
'''

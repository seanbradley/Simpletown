import requests, json

geo_data = open('testdata', 'w')

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
    
    data = r.text       

    geo_data.write(data)
    
geo_data.close()



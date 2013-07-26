'''
cities/fixtures/generate_testdata.py

This script will create a huge data file which you can load into Postgres with...

./manage.py loaddata testdata

...however, please note: presently, this script does not generate fully
valid JSON.  The above Django command will complain if you don't clean it
up.  In order for this data to function as a proper fixture, the script's
output will still require some manual pruning via additional regex processing,
or via a few simple replace/edits with the IDE of your choice.  Eventually,
this script will be refactored to create something more elegant...

Ultimately, you should have a single "testdata.json" file, containing
a simple Python list, and, in that list, nested dictionaries--one for each
geographic location pulled from the Small Business Association's (SBA) API.

Each of the nested dictionaries in the output file--or, more accurately--
in the resultant list, will be a single item in a single list, like so...

  [{...{...}}, {...{...}}, {...{...}} etc... ]

As of July 25, 2013, there are 5048 items or objects in the SBA list.  Once
it's cleaned up, and--if it were properly indented (optional) to make it
more human-readable--it should look like something like...

[{
  "pk": null,
  "model":"cities.city",
  "fields":
    {
      "county_name":"Mobile",
      "description":null,
      "feat_class":"Populated Place",
      "feature_id":"256",
      "fips_class":"C1",
      "fips_county_cd":"97",
      "full_county_name":"Mobile County",
      "link_title":null,
      "url":"http://townofdauphinisland.org/",
      "name":"Dauphin Island",
      "primary_latitude":"30.25",
      "primary_longitude":"-88.1",
      "state_abbreviation":"AL",
      "state_name":"Alabama"
    }
},

{
  "pk":null,
  "model":"cities.city",
  "fields":
    {
      "county_name": etc...
...

}]

Notice: only one square bracket at the beginning of the file, and one at
the end.  There are no square brackets in the body of the file.  Be certain,,
too, to clean out any extra or odd curly braces in the generated dataset.

In any case, running this script will get you started in the right direction.

'''

import re, requests, simplejson


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

    with open('testdata.json', 'a') as geo_data_file:

        simplejson.dump(data.replace('][][' , ',').replace('[]', ',').replace('][' , ',').replace(']" "[' , ',').replace('{' , '{"pk": null, "model": "cities.city", "fields": {').replace('}' , '}}'), geo_data_file)

geo_data_file.close()

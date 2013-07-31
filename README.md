#SIMPLETOWN
###a lightweight Django app fetching JSON data from an external API.

##ABOUT THE APP

You can see this app live at:

http://23.21.214.134/

E-mail me for username and password.  My contact info is below.

This app was actually a technical interview for a developer job, and was supposed to have been built from scratch and launched on AWS within 24-hours.

The app is intended to serve as the simplest barebones example or template of a Django implementation that fetches data from an external resource. It gathers USGS survey info from the Small Business Admnistration (SBA), which provides US Geographic Survey city names and associated data such as County, State, Latitude, and Longitude in JSON format via its own API.  (See http://www.sba.gov/about-sba-services/7617 for more info.)

The app has two views.  In view one: all cities and some associated data for each is fetched from the SBA's API and displayed as a list.  In view two: the database may be queried by county name, and only the cities within the requested county are subsequently displayed.

View one retrieves data dynamically from the SBA API via Kenneth Reitz's _Requests_ library; view two retrieves data from a PostgreSQL database, which was populated with city info by manually leveraging a large JSON fixture--the fixture itself being created from the the same SBA API.

##TECHNOLOGY STACK
Django, mod_wsgi, and Apache installed on an AWS EC2 server (Ubuntu Precise 12.04-i386; ami-def89fb7) associated with an Elastic IP. PostgreSQL is the database used in both the development and production environment.  Style provided courtesy of Bootstrap.

##TODO
-the virtualenv needs to be created with the --no-site-packages flag; this wasn't done on either the development machine nor the production machine, so the requirements.txt file may be a bit out of sync with regard to dependencies, and may require tweaking.
-view_one loads slowly; page caching helps after the page loads the first time, but perhaps it'd be nicer if the data were fetched asynchronously while displaying a throbber or progress bar.
-minor performance improvements might be enabled if static files were moved to S3 and retrieved from CloudFront CDN.


------------------------------------------------------------------------

##LICENSE

Copyright (c) 2013 by Sean Bradley.  All rights reserved.

You're free to use this code as however you like...pretty much.  You can even use it in closed-source, proprietary projects.

Here's the legalese:

Licensed under the Apache License, Version 2.0 (the “License”); you may not use this file except in compliance with the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an “AS IS” BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.


------------------------------------------------------------------------

##CONTACT

Your input is highly valued. Feel free to e-mail me directly and make suggestions or ask questions.  You can reach me via sean@blogblimp.com





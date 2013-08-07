#SIMPLETOWN
####a lightweight Django app fetching JSON data from an external API


###TECHNOLOGY STACK
Django, mod_wsgi, and Apache installed on an AWS EC2 server (Ubuntu Precise 12.04-i386) associated with an Elastic IP. PostgreSQL is the database used in both development and production.  Style provided courtesy of Bootstrap.  Validated HTML5/CSS3.

You can see a live example of the site at:

<http://23.21.214.134/>

* Username = ubuntu
* Password = ubuntu


###ABOUT SIMPLETOWN
This app evolved out of a technical interview.  The task: code from scratch a Django driven site with two views--one view that pulls in data from  a third-party API; another view with pulls in data from the app's own database.  Develop, integrate version control, and then deploy the whole thing on an AWS Linux instance within 24-hours.

_Voila'._  I give you Simpletown.

**Simpletown serves as a minimal, barebones example of a Django implementation that fetches data from an external resource.** It taps an API provided by the Small Business Admnistration (SBA), which provides US Geographic Survey city names and associated data (e.g., County, State, Latitude, and Longitude) in JSON format.  See <http://www.sba.gov/about-sba-services/7617> for more info about the API.

As mentioned, the app has two views.  View one retrieves data dynamically from the SBA's API via Kenneth Reitz's excellent _Requests_ library, and then cleans up the JSON and displays it as a list.  View two displays city info for a given county by querying a PostgreSQL database, which was populated with city info via manually leveraging a large JSON fixture--the fixture itself being created from the the same SBA API.


###USE SIMPLETOWN'S "FAST LANE" AMI FOR A RAPID LAUNCH
Your own copy of Simpletown is available and instantly deployable in less than five minutes if you purchase its Amazon Machine Image (AMI)...which is available for a one-time fee of just $5.  Save yourself the headache of backwards engineering the site from this repo; fahgeddabout configuring Apache and mod_wsgi. For the price of your carmel mocha machiatto (or a Redbull and Top Ramen), you can get past the boring Advil-laden part of deployment, and jump right into writing new models, new views, and styling your Django app as you see fit. Everything but e-mail settings are automagically configured for you in the FAST LANE AMI.


###STANDARD DEPLOYMENT
For best practices with regard to setting up your Django app see the _Two Scoops of Django_ project template and the associated book by Danny Greenfield and Audrey Roy:
<https://github.com/twoscoops/django-twoscoops-project>

With regard to app config, check out _The One True Way_ by Jacob Kaplan Moss:
<https://speakerdeck.com/jacobian/the-best-and-worst-of-django?slide=81>

Code is opinionated.  Here's an alternative to the above by Bruno Renié:
<http://bruno.im/2013/may/18/django-stop-writing-settings-files/>

You will need to change the following after launch...

In your Django settings file...
* ADMINS
* EMAIL_HOST_PASSWORD
* EMAIL_HOST_USER

In your Apache config file of your production machine, and the .bashrc of
your development machine...
* SECRET_KEY

In the .bashrc of your development machine...
* DEBUG


Set the SECRET_KEY and DEBUG as an environment variable on your development machine, like so...

    SECRET_KEY="your_secret_key"; export SECRET_KEY
    DEBUG="True"; export DEBUG

Or, make these settings permanent in your development environment via placing the following in ~/.bashrc, like so:

    SECRET_KEY = 'your_secret_key'
    DEBUG = 'True'

After adjusting these settings, remember to...

    touch .bashrc

If you're using a virtualenv--and you should-- _and_ you plan on running multiple environments on the same machine, you can place the above environment variable settings in your _bin/activate script_.  If you don't plan on running multiple environments on the same machine, just stick with placing the settings in the  _.bashrc_ file of your home directory.

Finally, i6
f you use a different e-mail provider than Gmail, you'll have to provide additional e-mail info in Django's settings file.


###STATIC ASSETS VS. MEDIA FILES
As in other web frameworks,  "media" directories are traditionally reserved for files uploaded by users, and "static" is the label applied to resources related to styling the site. Django has its own conventions in this regard, and can get rather nuanced in its efforts to keep things tidy and loosely coupled between "apps" within a single overarching project.  Particularly, it's careful with regard to namespacing of static files, so that each Django app within a project can contain its own static assets (i.e., css, js, and img files) without name conflicts.  Django provides a convenience function--_collectstatic_--to gather all of these resources into a common directory (the "static" directory) and to reference them via a common URL.  (See: <https://docs.djangoproject.com/en/dev/howto/static-files/>)

Many beginning Djangonauts find this process and its nomenclature a bit confusing.  Simpletown follows the convention of most Python and other web frameworks: it simply places all style related assets into one directory from the get go.  _Any_ file that has to do with styling of the site is labeled as "styles", and that's the directory in which you'll find it.  The "static" directory is empty--intentionally so--and should be left empty.  Manually placing files in the "static" directory will raise an ImproperlyConfigured exception. Presently, executing this command...

    ./manage.py collectstatic

...is still required to gather assets in the STYLE directory to the STATIC directory, and serve them up via the appropriate URL.

For styling related assets, Simpletown provides the following directories...

styles<br />
....site-styles<br />
........css<br />
........img<br />
........js<br />
....admin-styles<br />
........css<br />
........img<br />
........js<br />


###TODO
* the virtualenv needs to be created with the --no-site-packages flag; this wasn't done on either the development machine nor the production machine, so the requirements.txt file may be a bit out of sync with regard to dependencies, and may require tweaking.
* view_one loads slowly; page caching helps after the page loads the first time, but perhaps it'd be nicer if the data were fetched asynchronously while displaying a throbber or progress bar.
* minor performance improvements might be enabled if static files were moved to S3 and retrieved from CloudFront CDN.


------------------------------------------------------------------------

###LICENSE

Copyright (c) 2013 by Sean Bradley.  All rights reserved.

You're free to use this code as however you like...pretty much.  You can even use it in closed-source, proprietary projects.

Here's the legalese:

Licensed under the Apache License, Version 2.0 (the “License”); you may not use this file except in compliance with the License. You may obtain a copy of the License at

<http://www.apache.org/licenses/LICENSE-2.0>

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an “AS IS” BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.


------------------------------------------------------------------------

###CONTACT

Your input is highly valued. Feel free to e-mail me directly and make suggestions or ask questions.  You can reach me via sean@blogblimp.com
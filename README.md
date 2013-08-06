#SIMPLETOWN
###a lightweight Django app fetching JSON data from an external API


##TECHNOLOGY STACK
Django, mod_wsgi, and Apache installed on an AWS EC2 server (Ubuntu Precise 12.04-i386; ami-def89fb7) associated with an Elastic IP. PostgreSQL is the database used in both the development and production environment.  Style provided courtesy of Bootstrap.  Validated HTML5/CSS3.

You can see a live example of the site at:

http://23.21.214.134/

Username = ubuntu
Password = ubuntu


##ABOUT SIMPLETOWN
This app was actually a technical interview.  The task: code from scratch a Django driven site with two views--one view that pulls in data from  a third-party API; another view with pulls in data from the app's own database.  Develop, integrate version control, and then deploy the whole thing on an AWS Linux instance within 24-hours.

_Voila'._  I give you Simpletown.

As such, Simpletown serves as a minimal, barebones example of a Django implementation that fetches data from an external resource. It taps an API provided by the Small Business Admnistration (SBA), which provides US Geographic Survey city names and associated data (e.g., County, State, Latitude, and Longitude) in JSON format.  See http://www.sba.gov/about-sba-services/7617 for more info about the API.

The project is laid out so that the <repository_root> and <django_project_root> are the same.

As mentioned, the app has two views.  View one retrieves data dynamically from the SBA's API via Kenneth Reitz's excellent _Requests_ library, and then cleans up the JSON and displays it as a list.  View two displays city info for a given county by querying a PostgreSQL database, which was populated with city info via manually leveraging a large JSON fixture--the fixture itself being created from the the same SBA API.


##USE SIMPLETOWN'S "FAST LANE" AMI FOR RAPID AND EASY DEPLOYMENT
Your own copy of Simpletown is available and instantly deployable in less than five minutes if you purchase its Amazon Machine Image (AMI)...which is available for just $5.  Save yourself the headache of backwards engineering the site from this repo; fahgeddabout configuring Apache and mod_wsgi. For the price of your carmel mocha machiatto (or a Redbull and Top Ramen), you can get past the boring Advil-laden part of deployment, and jump right into writing new models and views, and styling your Django app as you see fit. Everything but e-mail settings are automagically configured for you in the FAST LANE AMI.


##STANDARD DEPLOYMENT
For best practices with regard to setting up your Django app see the _Two Scoops of Django_ project template and the associated book by Danny Greenfield and Audrey Roy:
https://github.com/twoscoops/django-twoscoops-project

With regard to app config, check out _The One True Way_ by Jacob Kaplan Moss:
https://speakerdeck.com/jacobian/the-best-and-worst-of-django?slide=81

Code is opinionated.  Here's an alternative to the above by Bruno Renié:
http://bruno.im/2013/may/18/django-stop-writing-settings-files/

In the settings.py, you will need to change the following after launch...

-ADMINS
-SECRET_KEY
-ALLOWED_HOSTS
-EMAIL_HOST_PASSWORD
-EMAIL_HOST_USER
-DEBUG


Set DEBUG as an environment variable, like so...

    DEBUG="True"; export DEBUG

Or, make it permanent in your development environment via placing the
following in ~/.bashrc, like so:

    DEBUG = 'True'

Remember to "touch .bashrc" after doing so.

You also need to set an original SECRET_KEY

 ...and...

You need to change ALLOWED_HOSTS to the URL for your individual AWS EC2 instance, or to an AWS Elastic IP, or your actual custom domain.


If you use a different e-mail provider than Gmail, you'll have to configure additional e-mail settings.


##STATIC FILES
Django can get rather nuanced with the way it deals with static files.  Particularly, it's careful with regard to namespacing of static files.

See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
And: https://docs.djangoproject.com/en/dev/howto/static-files/

Typically, "manage.py collectstatic" gathers all static files included in STATICFILES_DIRS into the STATIC_ROOT directory.  Also, typically, STATIC_ROOT is called "assets".  But, for ease of this deployment, all
the static and style-related files (except for admin styles) are already in one directory. So, we're pointing STATIC_ROOT to that directory.  It's presently set up like so, to enable the easy drop-in of separate stylesheets for the admin dashboard:

static
    site-styles
        css
        img
        js
    admin-styles
        css
        img
        js


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





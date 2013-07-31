from django.db import models


class City(models.Model):
    county_name = models.CharField('county_name', max_length = 255, null=True, blank=True)
    description = models.TextField('description', max_length = 250, null=True, blank=True)
    feat_class = models.CharField('feat_class', max_length = 255, null=True, blank=True)
    feature_id = models.IntegerField('feature_id', default = 0, null=True, blank=True)
    fips_class = models.CharField('fips_class', max_length = 2, null=True, blank=True)
    fips_county_cd = models.CharField('fips_county_cd', max_length = 255, null=True, blank=True)
    full_county_name = models.CharField('full_county_name', max_length = 255, null=True, blank=True)
    link_title = models.CharField('link_title', max_length = 255, null=True, blank=True)
    url = models.CharField('url', max_length = 255, null=True, blank=True)
    name = models.CharField('name', max_length = 255, null=True, blank=True)
    primary_latitude = models.DecimalField('primary_latitude', max_digits = 6, decimal_places = 3, null=True, blank=True)
    primary_longitude = models.DecimalField('primary_longitude', max_digits = 6, decimal_places = 3, null=True, blank=True)
    state_abbreviation = models.CharField('state_abbreviation', max_length = 2, null=True, blank=True)
    state_name = models.CharField('state_name', max_length = 25, null=True, blank=True)

    class Meta:
        ordering = ["name"]

    def __unicode__(self):
        return self.name


'''
# Here's the raw SQL--which, if syncdb or South does what it's supposed
# to do, you shouldn't need in order to create the appropriate table
# in Postgres prior to loading the JSON data.  But, just in case, you
# can align the db with the above model and prep it for the testdata.json
# via ./manage.py dbshell with...

BEGIN;

CREATE TABLE "cities_city" (
    "id" serial NOT NULL PRIMARY KEY,
    "county_name" varchar(255),
    "description" text,
    "feat_class" varchar(255),
    "feature_id" integer,
    "fips_class" varchar(2),
    "fips_county_cd" varchar(255),
    "full_county_name" varchar(255),
    "link_title" varchar(255),
    "url" varchar(255),
    "name" varchar(255),
    "primary_latitude" numeric(6, 3),
    "primary_longitude" numeric(6, 3),
    "state_abbreviation" varchar(2),
    "state_name" varchar(25)
)
;

COMMIT;

'''
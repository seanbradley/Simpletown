from django.db import models


class City(models.Model):
    county_name = models.CharField(max_length = 100),
    description = models.TextField(null=True, blank=False),
    feat_class = models.CharField(max_length = 50),
    feature_id = models.CharField(max_length = 5),
    fips_class = models.CharField(max_length = 2),
    fips_county_cd = models.CharField(max_length = 3),
    full_county_name = models.CharField(max_length = 100),
    link_title = models.CharField(max_length = 50, null=True, blank=False),
    url = models.URLField(max_length = 200),
    name = models.CharField(max_length = 50),
    primary_latitude = models.DecimalField(may_length = 5, decimal_places = 2),
    primary_longitude = models.DecimalField(may_length = 5, decimal_places = 2),
    state_abbreviation = models.CharField(max_length = 2),
    state_name = models.CharField(max_length = 50
    
    def __unicode__(self):
            return u'%s %s %s %s' % (self.county_name, self.name, self.primary_latitude, self.primary_longitude)

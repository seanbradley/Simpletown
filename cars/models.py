import operator
from django.db import models
from django.db.models import Q
from djangoyearlessdate.models import YearField


class CarManager(models.Manager):
    def search(self, term):
        pass

class Car(models.Model):
    vsn = models.CharField('vsn', max_length = 12, null=False, blank=True)
    trim_id = models.IntegerField('trim_id', default = 0, null=True, blank=True)
    vehicle_year = YearField('vehicle_year', default = 0, null=True, blank=True)
    make = models.CharField('make', max_length = 100, null=False, blank=True)
    vehicle_model = models.CharField('vehicle_model', max_length = 3, null=False, blank=True)
    trim_name = models.TextField('trim_name', max_length = 250, null=False, blank=True)
    objects = CarManager()

    class Meta:
        ordering = ["vsn"]

    def __unicode__(self):
        return u'%s %s %s -- %s (Trim ID: %s)' % (self.vehicle_year, self.make, self.vehicle_model, self.trim_name, self.trim_id)
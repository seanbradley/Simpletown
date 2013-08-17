import operator
from django.db import models
from django.db.models import Q
#from django.core.resolvers import reverse
from djangoyearlessdate.models import YearField

class CarManager(models.Manager):
    def search(self, search_terms):
        terms = [term.strip() for term in search_terms.split()]
        q_objects = []

        for term in terms:
            q_objects.append(Q(vsn__icontains=term))
            #q_objects.append(Q(trim_id__icontains=term))
            #q_objects.append(Q(vehicle_year__icontains=term))
            #q_objects.append(Q(trim_name__icontains=term))
            #q_objects.append(Q(trim_id__icontains=term))

        # Start with a bare QuerySet
        qs = self.get_query_set()

        # Use operator's or_ to string together all of your Q objects.
        return qs.filter(reduce(operator.or_, q_objects))


class Car(models.Model):
    vsn = models.CharField('vsn', max_length = 12, null=False, blank=True)
    trim_id = models.IntegerField('trim_id', default = 0, null=True, blank=True)
    vehicle_year = YearField('vehicle_year', default = 0, null=True, blank=True)
    #vehicle_year = models.CharField('vehicle_year', max_length = 4, null=False, blank=True)
    make = models.CharField('make', max_length = 100, null=False, blank=True)
    vehicle_model = models.CharField('vehicle_model', max_length = 3, null=False, blank=True)
    trim_name = models.TextField('trim_name', max_length = 250, null=False, blank=True)
    objects = CarManager()

    class Meta:
        ordering = ["vsn"]

    #def get_absolute_url(self):
    #    return reverse("car_list")

    def __unicode__(self):
        return self.vsn, self.trim_id, self.vehicle_year, self.make, self.vehicle_model,
        self.trim_name

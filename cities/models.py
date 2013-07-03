from django.db import models

class City(models.Model):
    county = models.CharField(max_length=200)

from django.db import models

class Cities(models.Model):
    county = models.CharField(max_length=200)

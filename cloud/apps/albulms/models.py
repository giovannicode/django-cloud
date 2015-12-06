from __future__ import unicode_literals

from django.contrib.gis.db import models

class Albulm(models.Model):
    name = models.CharField(max_length=60, blank=False)

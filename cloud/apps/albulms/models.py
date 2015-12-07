from __future__ import unicode_literals

from django.contrib.gis.db import models

from apps.artists.models import Artist


class Albulm(models.Model):
    name = models.CharField(max_length=60, blank=False)
    artist = models.ForeignKey(Artist)

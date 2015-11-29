from django.contrib.gis.db import models

# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=60, blank=False)

    def __unicode__(self):
        return self.name

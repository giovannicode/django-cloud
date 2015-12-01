from django.contrib.gis.db import models

class Genre(models.Model):
    name = models.CharField(max_length=60)

    def __unicode__(self):
        return self.name

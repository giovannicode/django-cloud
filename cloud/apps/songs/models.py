from django.contrib.gis.db import models

# Create your models here.
class Song(models.Model):
    soundfile = models.FileField()
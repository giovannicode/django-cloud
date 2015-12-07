from django.contrib.gis.db import models

from apps.artists.models import Artist 
from apps.genres.models import Genre
from apps.albulms.models import Albulm

import uuid
import os

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return filename

class Song(models.Model):
    artist = models.ForeignKey(Artist)
    albulm = models.ForeignKey(Albulm)
    track_number = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=60, blank=False)
    soundfile = models.FileField(upload_to=get_file_path)
    lyrics = models.TextField(null=True, blank=True)
    genre = models.ForeignKey(Genre)

    def __unicode__(self):
        return self.artist.name + " - " + self.name

from django.contrib.gis.db import models
from .utils import get_file_path


class Video(models.Model):
    name = models.CharField(max_length=60)
    video_file = models.FileField(upload_to=get_file_path)
    
    def __unicode__(self):
        return self.name

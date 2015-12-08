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


def get_final_filename(d):
    
    return d['filename']


def download_soundfile(self):

    song_url=self.soundfile_url
    uuid_filename = uuid.uuid4()

    ydl_opts = {
        'outtmpl': '/website/files/media/' + str(uuid_filename) + '.%(ext)s',
        'format': 'bestaudio',
        'postproccesors': [{
            'key': 'FFmpegExtractAudio',
             'preferredquality': '1411',
        }],
        'progress_hooks': [get_final_filename],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([song_url])
    return 


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

    def download_soundfile(self):

        def get_final_filename(d):
            global self.soundfile
            self.soundfile = d['filename']

        song_url=self.soundfile_url
        uuid_filename = uuid.uuid4()

        ydl_opts = {
            'outtmpl': '/website/files/media/' + str(uuid_filename) + '.%(ext)s',
            'format': 'bestaudio',
            'postproccesors': [{
                'key': 'FFmpegExtractAudio',
                 'preferredquality': '1411',
            }],
            'progress_hooks': [get_final_filename],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([song_url])
  
    def save(self, *args, **kwargs):
        try:
            song = Song.objects.get(pk=self.pk)
        except: 
        if self.soundfile_url != song.soundfile_url
            self.download_soundfile()

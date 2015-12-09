import uuid

import youtube_dl

from django.contrib.gis.db import models
from django.conf import settings


from apps.artists.models import Artist 
from apps.genres.models import Genre
from apps.albulms.models import Albulm


#def get_file_path(instance, filename):
#    ext = filename.split('.')[-1]
#    filename = "%s.%s" % (uuid.uuid4(), ext)
#    return filename
#
#
#def get_final_filename(d):
#    
#    return d['filename']
#
#
#def download_soundfile(self):
#
#    song_url=self.soundfile_url
#    uuid_filename = uuid.uuid4()
#
#    ydl_opts = {
#        'outtmpl': '/website/files/media/' + str(uuid_filename) + '.%(ext)s',
#        'format': 'bestaudio',
#        'postproccesors': [{
#            'key': 'FFmpegExtractAudio',
#             'preferredquality': '1411',
#        }],
#        'progress_hooks': [get_final_filename],
#    }
#
#    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#        ydl.download([song_url])
#    return 


class Song(models.Model):
    artist = models.ForeignKey(Artist)
    albulm = models.ForeignKey(Albulm, null=True, blank=True)
    track_number = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=60, blank=False)
    soundfile = models.FileField(blank=True)
    soundfile_url = models.URLField()
    lyrics = models.TextField(null=True, blank=True)
    genre = models.ForeignKey(Genre)

    def __unicode__(self):
        return self.artist.name + " - " + self.name

    def download_soundfile(self):
        soundfile = self.soundfile        

        def add_file_to_object(d):
            global soundfile
            filename = d['filename'].replace(settings.MEDIA_ROOT, '')
            self.soundfile = filename

        song_url=self.soundfile_url
        uuid_filename = uuid.uuid4()

        ydl_opts = {
            'outtmpl': '/website/files/media/' + str(uuid_filename) + '.%(ext)s',
            'format': 'bestaudio',
            'postproccesors': [{
                'key': 'FFmpegExtractAudio',
                 'preferredquality': '1411',
            }],
            'progress_hooks': [add_file_to_object],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([song_url])
  
    def save(self, *args, **kwargs):
        try:
            song = Song.objects.get(pk=self.pk)
            if self.soundfile_url != song.soundfile_url:
                self.download_soundfile()
        except: 
            self.download_soundfile()
        super(Song, self).save(*args, **kwargs)

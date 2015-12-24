from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Artist

class ArtistView(TemplateView):
    template_name = 'artists/artist_songs_list.html'

    def get_context_data(self, **kwargs):
        context = super(ArtistView, self).get_context_data(**kwargs)
        artist_id = kwargs['artist']
        artist = Artist.objects.get(id=artist_id)
        songs = artist.song_set.order_by('name')
        context['songs'] = songs
        return context

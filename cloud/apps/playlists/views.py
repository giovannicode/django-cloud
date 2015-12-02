from django.shortcuts import render

from django.views.generic import TemplateView

from apps.songs.models import Song

class RandomPlaylistView(TemplateView):
     template_name = 'playlists/random_playlist.html'

     def get_context_data(self, **kwargs):
         context = super(RandomPlaylistView, self).get_context_data(**kwargs)
         context['song'] = Song.objects.order_by('?')[0]
         return context

from django.shortcuts import render

from django.views.generic import TemplateView

from apps.songs.models import Song

class RandomPlaylistView(TemplateView):
     template_name = 'playlists/playlist.html'

     def get_context_data(self, **kwargs):
         context = super(RandomPlaylistView, self).get_context_data(**kwargs)
         context['song'] = Song.objects.order_by('?')[0]
         return context

class GenresPlaylistView(TemplateView):
     template_name = 'playlists/playlist.html'

     def get_context_data(self, **kwargs):
         context = super(GenresPlaylistView, self).get_context_data(**kwargs)
         genre = kwargs['genre']
         context['song'] = Song.objects.filter(genre=genre).order_by('?')[0]
         return context

class ArtistPlaylistView(TemplateView):
     template_name = 'playlists/playlist.html'

     def get_context_data(self, **kwargs):
         context = super(ArtistPlaylistView, self).get_context_data(**kwargs)
         artist = kwargs['artist']
         context['song'] = Song.objects.filter(artist=artist).order_by('?')[0]
         return context

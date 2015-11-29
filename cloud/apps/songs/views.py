from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class PlaySongView(TemplateView):
    template_name = 'songs/play_song.html' 

from django.conf.urls import url, patterns
from django.conf.urls.static import static
from django.conf import settings

import views

urlpatterns = [
    url(r'random/', views.RandomPlaylistView.as_view(), name='random'),
    url(r'genres/(?P<genre>[\w-]+)/', views.GenresPlaylistView.as_view(), name='genres'),
    url(r'artists/(?P<artist>[\w-]+)/', views.ArtistPlaylistView.as_view(), name='artists'),
    url(r'songs/(?P<song>[\w-]+)/', views.SongsPlaylistView.as_view(), name='songs'),
    #url(r'albulms/(?P<albulms>[\w-]+)/', views.AlbulmsPlaylistView.as_view(), name='albulms'),
]

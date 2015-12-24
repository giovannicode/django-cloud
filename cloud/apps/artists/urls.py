from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
    url(r'artist/(?P<artist>[\w-]+)/', views.ArtistView.as_view(), name='artist'),
)

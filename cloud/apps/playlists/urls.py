from django.conf.urls import url, patterns
from django.conf.urls.static import static
from django.conf import settings

import views

urlpatterns = [
    url(r'random/', views.RandomPlaylistView.as_view(), name='random'),
]

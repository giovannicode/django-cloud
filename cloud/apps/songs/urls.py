from django.conf.urls import url, patterns
from django.conf.urls.static import static
from django.conf import settings

import views

urlpatterns = [
    url(r'play/', views.PlaySongView.as_view(), name='play'),
]

from django.contrib import admin
from .models import Song, Artist

class SongAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'get_artist_name', 'name')
    ordering = ('artist__name', 'name')

    def get_artist_name(self, obj):
        return obj.artist.name

    get_artist_name.admin_order_field = "artist__name"
    get_artist_name.short_description = "Artist"


admin.site.register(Song, SongAdmin)

from django.contrib import admin
from .models import Genre

class GenreAdmin(admin.ModelAdmin):
    pass

admin.site.register(Genre, GenreAdmin)

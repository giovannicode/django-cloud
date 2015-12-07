from django.contrib import admin

from .models import Albulm

class AlbulmAdmin(admin.ModelAdmin):
    pass

admin.site.register(Albulm, AlbulmAdmin)

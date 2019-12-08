from django.contrib import admin
from .models import Playlist, Song, Opinion

class SongAdminInline(admin.StackedInline):
    model = Song
    can_delete = True

class SongAdmin(admin.ModelAdmin):
    inlines = (SongAdminInline,) 

admin.site.register(Playlist, SongAdmin)
admin.site.register(Opinion)
from rest_framework import serializers
from .models import Song, Playlist, Opinion

class SongSerializer(serializers.ModelSerializer):
    allow_null = True
    many = True

    class Meta:
        model = Song
        fields = ['title','url']

class PlaylistSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ['title',]
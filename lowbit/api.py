from .models import Playlist, Song, Opinion
from .serializers import SongSerializer, PlaylistSeralizer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

'''
find song

import playlist
'''

class playlistylistList(APIView):
    '''
    List all playlist, or create new one

    create
        {
        "title":"123"
        }
    '''

    def get(self, request, format=None):
        obj = Playlist.objects.all()#filter(user=self.request.user)
        serializer = PlaylistSeralizer(obj, many=True)
        return Response(serializer.data)

    def put(self, request, format=None):
        serializer = PlaylistSeralizer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

class PlaylistDetail(APIView):
    """
    Retrieve playlist, songs by specific playlist and update, delete a playlist instance.
    """

    def get_playlist(self, pk):
        try:
            return Playlist.objects.get(pk=pk)
        except Playlist.DoesNotExist:
            raise Http404


    def get_song(self, pk):
        try:
            return Song.objects.filter(song__user=self.request.user).filter(song_id=pk)
        except Song.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        obj = self.get_song(pk)
        serializer = SongSerializer(obj, many=True)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        obj = self.get_playlist(pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SongDetail(APIView):
    """
    Add, delete song.
    """

    def get_song(self, pk):
        try:
            return Song.objects.filter(song__user=self.request.user).filter(id=pk)
        except Song.DoesNotExist:
            raise Http404

    def put(self, request, format=None):
        serializer = SongSeralizer(data=request.data)
        if serializer.is_valid():
            serializer.save(song=pk)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, pk, format=None):
        obj = self.get_song(pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
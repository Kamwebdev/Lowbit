from django.db import models
from django.contrib.auth.models import User


class Playlist(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return ("email: %s, playlista: %s" % (self.user.email, self.title))


class Song(models.Model):
    title = models.CharField(max_length=50,)
    url = models.CharField(max_length=50,)
    song = models.ForeignKey(Playlist, on_delete=models.CASCADE)

    def __str__(self):
        return ("%s" % (self.title))


class Opinion(models.Model):
    sugestion = models.TextField(max_length=500,)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return ("%s" % (self.user.email))

from django.db import models

from dt_bands.models.band_member import BandMember
from dt_genres.models.genre import Genre


class Band(models.Model):
    band_name = models.CharField(max_length=100)
    band_country = models.CharField(max_length=100)
    band_formed_in = models.IntegerField()
    band_description = models.TextField()
    band_genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='genres')
    band_members = models.ManyToManyField(BandMember, related_name='members')

    def __str__(self):
        return self.band_name

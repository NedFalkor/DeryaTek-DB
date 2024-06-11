from django.db import models
from dt_gigs.models.gig import Gig


class Setlist(models.Model):
    gig = models.ForeignKey(Gig, on_delete=models.CASCADE, related_name='setlist')
    song_number = models.IntegerField()
    song_title = models.CharField(max_length=255)
    song_duration = models.DurationField(blank=True, null=True)
    album_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        unique_together = ('gig', 'song_number')
        ordering = ['song_number']

    def __str__(self):
        return f"{self.song_number}. {self.song_title} ({self.gig.band})"

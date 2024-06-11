from django.db import models
from dt_records.models.record import Record


class Tracklist(models.Model):
    record = models.ForeignKey(Record, on_delete=models.CASCADE, related_name='tracklist')
    song_number = models.IntegerField()
    song_title = models.CharField(max_length=255)
    song_duration = models.DurationField(blank=True, null=True)
    side = models.CharField(max_length=1, choices=[('A', 'Side A'), ('B', 'Side B')], default='A')

    class Meta:
        unique_together = ('record', 'song_number', 'side')
        ordering = ['side', 'song_number']

    def __str__(self):
        return f"{self.song_number}. {self.song_title} ({self.record.record_title})"

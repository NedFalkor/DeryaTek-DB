from django.db import models

from dt_bands.models.band import Band
from dt_records.models.label import Label
from dt_genres.models.genre import Genre
from dt_genres.models.style import Style


class Record(models.Model):
    FORMAT_CHOICES = [
        ('CD', 'CD'),
        ('Vinyl', 'Vinyl'),
        ('Concert Live', 'Concert Live'),
    ]

    CONDITION_CHOICES = [
        ('New', 'Neuf'),
        ('Used', 'Occasion'),
        ('Damaged', 'Endommagé'),
        ('Broken', 'Cassé')
    ]

    TYPE_CHOICES = [
        ('Official', 'Officiel'),
        ('Bootleg', 'Bootleg'),
        ('Burned', 'CD Gravé')
    ]

    record_band = models.ForeignKey(Band, on_delete=models.CASCADE, related_name='records')
    record_condition = models.CharField(max_length=50, choices=CONDITION_CHOICES)
    record_cover = models.ImageField(upload_to='record_covers/', blank=True, null=True)
    record_format = models.CharField(max_length=50, choices=FORMAT_CHOICES)
    record_genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='records')
    record_label = models.ForeignKey(Label, on_delete=models.CASCADE)
    record_style = models.ForeignKey(Style, on_delete=models.CASCADE, related_name='records')
    record_title = models.CharField(max_length=100)
    record_tracklist = models.TextField(blank=True, null=True)
    record_tracklist_side_b = models.TextField(blank=True, null=True)
    record_year = models.DateField()
    record_type = models.CharField(max_length=50, choices=TYPE_CHOICES, default='Official')

    def __str__(self):
        return self.record_title

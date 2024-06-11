from django.db import models
from dt_bands.models.band import Band
from dt_bands.models.band_member import BandMember
from dt_records.models.label import Label
from dt_genres.models.genre import Genre
from dt_genres.models.style import Style
from dt_genres.models.sub_genre import SubGenre


class Record(models.Model):
    FORMAT_CHOICES = [
        ('CD', 'CD'),
        ('Vinyl 33 RPM', 'Vinyl 33 RPM'),
        ('Vinyl 45 RPM', 'Vinyl 45 RPM'),
        ('Audio Live Concert', 'Concert Audio'),
        ('Video Live Concert', 'Concert Vidéo'),
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

    LENGTH_CHOICES = [
        ('Full-length', 'Full-length'),
        ('EP', 'EP')
    ]

    record_band = models.ForeignKey(Band, on_delete=models.CASCADE, related_name='records')
    record_condition = models.CharField(max_length=50, choices=CONDITION_CHOICES)
    record_cover = models.ImageField(upload_to='record_covers/', blank=True, null=True)
    record_format = models.CharField(max_length=50, choices=FORMAT_CHOICES)
    record_genres = models.ManyToManyField(Genre, related_name='records')
    record_sub_genres = models.ManyToManyField(SubGenre, related_name='records', blank=True)
    record_styles = models.ManyToManyField(Style, related_name='records')
    record_label = models.ForeignKey(Label, on_delete=models.CASCADE)
    record_title = models.CharField(max_length=100)
    record_tracklist = models.TextField(blank=True, null=True)
    record_tracklist_side_b = models.TextField(blank=True, null=True)
    record_year = models.DateField()
    record_type = models.CharField(max_length=50, choices=TYPE_CHOICES, default='Official')
    record_length = models.CharField(max_length=50, choices=LENGTH_CHOICES, default='Full-length')
    record_band_members = models.ManyToManyField(BandMember, related_name='records')

    def __str__(self):
        return self.record_title

from django.db import models
from dt_bands.models.band_member import BandMember
from dt_genres.models.genre import Genre


class Band(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('hiatus', 'On Hiatus'),
        ('split_up', 'Split Up'),
    ]

    band_name = models.CharField(max_length=100)
    band_country = models.CharField(max_length=100)
    band_formed_in = models.IntegerField()
    band_description = models.TextField()
    band_genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='genres')
    band_members = models.ManyToManyField(BandMember, related_name='members')
    band_photo = models.ImageField(upload_to='band_photos/', blank=True, null=True)
    band_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')  # New field for status
    band_separation_date = models.DateField(blank=True, null=True)  # New field for separation date

    def __str__(self):
        return self.band_name

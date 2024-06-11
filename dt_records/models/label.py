from django.db import models

from dt_genres.models.genre import Genre
from dt_genres.models.style import Style
from dt_genres.models.sub_genre import SubGenre


class Label(models.Model):
    STATUS_CHOICES = [
        ('Actif', 'Actif'),
        ('Inactif', 'Inactif'),
        ('Temporairement indisponible', 'Temporairement indisponible'),
    ]

    label_address = models.CharField(max_length=255,blank=True, null=True)
    label_country = models.CharField(max_length=100,blank=True, null=True)
    label_description = models.TextField(blank=True, null=True)
    label_founding_date = models.DateField(blank=True, null=True)
    label_name = models.CharField(max_length=100)
    label_phone_number = models.CharField(max_length=20, blank=True, null=True)
    label_photo = models.ImageField(upload_to='label_photos/', blank=True, null=True)
    label_postal_code = models.CharField(max_length=20,blank=True, null=True)
    label_status = models.CharField(max_length=50, choices=STATUS_CHOICES,blank=True, null=True)
    label_genres = models.ManyToManyField(Genre, related_name='labels')
    label_styles = models.ManyToManyField(Style, related_name='labels')
    label_sub_genres = models.ManyToManyField(SubGenre, related_name='labels')

    def __str__(self):
        return self.label_name

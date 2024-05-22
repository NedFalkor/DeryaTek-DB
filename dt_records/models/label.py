from django.db import models

from dt_genres.models.genre import Genre
from dt_genres.models.style import Style


class Label(models.Model):
    STATUS_CHOICES = [
        ('Actif', 'Actif'),
        ('Inactif', 'Inactif'),
        ('Temporairement indisponible', 'Temporairement indisponible'),
    ]

    label_address = models.CharField(max_length=255)
    label_country = models.CharField(max_length=100)
    label_description = models.TextField()
    label_founding_date = models.DateField()
    label_name = models.CharField(max_length=100)
    label_phone_number = models.CharField(max_length=20, blank=True, null=True)
    label_photo = models.ImageField(upload_to='label_photos/', blank=True, null=True)
    label_postal_code = models.CharField(max_length=20)
    label_status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    label_genres = models.ManyToManyField(Genre, related_name='labels')
    label_styles = models.ManyToManyField(Style, related_name='labels')

    def __str__(self):
        return self.label_name

from django.db import models

from dt_genres.models.genre import Genre


class Style(models.Model):
    style_name = models.CharField(max_length=100)
    style_description = models.TextField()
    style_photo = models.ImageField(upload_to='style_photos/', blank=True, null=True)
    style_genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='styles')

    def __str__(self):
        return self.style_name

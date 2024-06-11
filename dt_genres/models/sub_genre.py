from django.db import models
from dt_genres.models.style import Style


class SubGenre(models.Model):
    sub_genre_name = models.CharField(max_length=100)
    sub_genre_description = models.TextField()
    sub_genre_photo = models.ImageField(upload_to='sub_genre_photos/', blank=True, null=True)
    sub_genre_styles = models.ManyToManyField(Style, related_name='sub_genres')

    def __str__(self):
        return self.sub_genre_name

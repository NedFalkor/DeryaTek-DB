from django.db import models


class Genre(models.Model):
    genre_name = models.CharField(max_length=100)
    genre_description = models.TextField()
    genre_photo = models.ImageField(upload_to='genre_photos/', blank=True, null=True)

    def __str__(self):
        return self.genre_name

from django.db import models


class Venue(models.Model):
    venue_name = models.CharField(max_length=255)
    venue_address = models.CharField(max_length=500)
    venue_capacity = models.IntegerField()
    venue_country = models.CharField(max_length=100, blank=True, null=True)
    venue_city = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.venue_name

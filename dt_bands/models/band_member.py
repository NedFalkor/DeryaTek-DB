from django.db import models
from dt_bands.models.instrument import Instrument


class BandMember(models.Model):
    band_member_first_name = models.CharField(max_length=100)
    band_member_last_name = models.CharField(max_length=100, blank=True, null=True)
    band_member_birth_city = models.CharField(max_length=100)
    band_member_birth_country = models.CharField(max_length=100, blank=True, null=True)
    band_member_nationality = models.CharField(max_length=100, blank=True, null=True)
    band_member_birth_year = models.IntegerField()
    band_member_death_year = models.IntegerField(blank=True, null=True)
    band_member_instruments = models.ManyToManyField(Instrument, blank=True)
    band_member_photo = models.ImageField(upload_to='member_photos/', blank=True, null=True)

    def __str__(self):
        return f"{self.band_member_first_name} {self.band_member_last_name}"

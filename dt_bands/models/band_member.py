from django.db import models

from dt_bands.models.instrument import Instrument


class BandMember(models.Model):
    band_member_name = models.CharField(max_length=100)
    band_member_birth_year = models.IntegerField()
    band_member_country = models.CharField(max_length=100)
    band_member_instrument = models.ForeignKey(Instrument, on_delete=models.SET_NULL, null=True, blank=True)
    band_member_photo = models.ImageField(upload_to='member_photos/', blank=True, null=True)

    def __str__(self):
        return self.band_member_name

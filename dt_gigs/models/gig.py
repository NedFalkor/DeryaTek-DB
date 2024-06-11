from django.db import models
from dt_bands.models.band import Band
from dt_gigs.models.venue import Venue


class Gig(models.Model):
    band = models.ForeignKey(Band, on_delete=models.CASCADE, related_name='gigs')
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name='gigs')
    gig_date = models.DateTimeField()
    gig_ticket_price = models.DecimalField(max_digits=8, decimal_places=2)
    gig_link = models.URLField(blank=True, null=True)
    gig_additional_info = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.band} at {self.venue} on {self.gig_date.strftime('%Y-%m-%d %H:%M')}"

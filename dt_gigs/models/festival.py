from django.db import models
from dt_bands.models.band import Band
from dt_gigs.models.venue import Venue
from dt_gigs.models.gig import Gig  # Assurez-vous que l'importation est correcte


class Festival(models.Model):
    festival_name = models.CharField(max_length=255)
    festival_start_date = models.DateField()
    festival_end_date = models.DateField()
    venues = models.ManyToManyField(Venue, related_name='festivals')
    bands = models.ManyToManyField(Band, related_name='festivals')
    gigs = models.ManyToManyField(Gig, related_name='festivals', blank=True)
    festival_description = models.TextField(blank=True, null=True)
    festival_link = models.URLField(blank=True, null=True)
    festival_ticket_price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.festival_name} ({self.festival_start_date} - {self.festival_end_date})"

    @property
    def is_current(self):
        from django.utils.timezone import now
        return self.festival_start_date <= now().date() <= self.festival_end_date

from django.db import models


class Instrument(models.Model):
    INSTRUMENT_CATEGORY = sorted([
        ('wind', 'Wind'),
        ('strings', 'Strings'),
        ('percussion', 'Percussion'),
        ('electronic', 'Electronic'),
        ('keyboard', 'Keyboard'),
        ('brass', 'Brass'),
        ('woodwind', 'Woodwind'),
        ('vocal', 'Vocal')
    ], key=lambda choice: choice[1])

    instrument_name = models.CharField(max_length=100, unique=True)
    instrument_description = models.TextField(blank=True, null=True)
    instrument_category = models.CharField(max_length=50, choices=INSTRUMENT_CATEGORY, blank=True, null=True)

    def __str__(self):
        return self.instrument_name

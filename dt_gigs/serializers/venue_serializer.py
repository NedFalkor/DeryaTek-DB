from rest_framework import serializers

from dt_gigs.models.venue import Venue


class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = '__all__'


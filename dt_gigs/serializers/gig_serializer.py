from rest_framework import serializers

from dt_gigs.models.gig import Gig


class GigSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gig
        fields = '__all__'

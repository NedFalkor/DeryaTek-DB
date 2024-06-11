from rest_framework import serializers

from dt_gigs.models.festival import Festival


class FestivalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Festival
        fields = '__all__'

from rest_framework import serializers
from dt_records.models.tracklist import Tracklist


class TracklistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tracklist
        fields = '__all__'

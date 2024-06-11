from rest_framework import serializers
from dt_gigs.models.setlist import Setlist


class SetlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setlist
        fields = '__all__'

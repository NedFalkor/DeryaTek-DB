from rest_framework import serializers

from dt_bands.models import BandMember


class BandMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = BandMember
        fields = '__all__'

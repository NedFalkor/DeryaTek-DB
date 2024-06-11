from rest_framework import serializers

from dt_bands.models.instrument import Instrument


class InstrumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instrument
        fields = '__all__'

from rest_framework import serializers

from dt_records.models.record import Record


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = [
            'id', 'record_band', 'record_condition', 'record_cover',
            'record_format', 'record_genre', 'record_label', 'record_style', 'record_title',
            'record_tracklist', 'record_tracklist_side_b', 'record_year', 'record_type'
        ]
        extra_kwargs = {
            'record_cover': {'required': False, 'allow_null': True}
        }

    def to_representation(self, instance):
        representation = super(RecordSerializer, self).to_representation(instance)
        representation['record_band'] = instance.record_band.band_name
        representation['record_genre'] = instance.record_genre.genre_name
        representation['record_label'] = instance.record_label.label_name
        representation['record_style'] = instance.record_style.style_name
        return representation

from rest_framework import serializers
from dt_records.models.record import Record


class RecordSerializer(serializers.ModelSerializer):
    record_band_members = serializers.StringRelatedField(many=True)

    class Meta:
        model = Record
        fields = [
            'id', 'record_band', 'record_condition', 'record_cover',
            'record_format', 'record_genre', 'record_sub_genre', 'record_style', 'record_label', 'record_title',
            'record_tracklist', 'record_tracklist_side_b', 'record_year', 'record_type', 'record_band_members'
        ]
        extra_kwargs = {
            'record_cover': {'required': False, 'allow_null': True}
        }

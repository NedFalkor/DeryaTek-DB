from rest_framework import serializers

from dt_genres.serializers.genre_serializer import GenreSerializer
from dt_genres.serializers.style_serializer import StyleSerializer
from dt_records.models.label import Label


class LabelSerializer(serializers.ModelSerializer):
    label_genres = GenreSerializer(many=True, read_only=True)
    label_styles = StyleSerializer(many=True, read_only=True)

    class Meta:
        model = Label
        fields = '__all__'

from rest_framework import serializers

from dt_genres.models.style import Style
from dt_genres.serializers.genre_serializer import GenreSerializer


class StyleSerializer(serializers.ModelSerializer):
    style_genre = GenreSerializer()

    class Meta:
        model = Style
        fields = '__all__'

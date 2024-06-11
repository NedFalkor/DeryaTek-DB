from rest_framework import serializers
from dt_genres.models.sub_genre import SubGenre
from dt_genres.serializers.style_serializer import StyleSerializer


class SubGenreSerializer(serializers.ModelSerializer):
    sub_genre_styles = StyleSerializer(many=True)

    class Meta:
        model = SubGenre
        fields = '__all__'

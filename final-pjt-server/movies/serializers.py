from rest_framework import serializers
from .models import Genre, Movie, Rating


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'
        # fields = ('id', 'title', 'completed',)

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'
        # fields = ('id', 'title', 'completed',)

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'
        read_only_fields = ('user', 'movie')
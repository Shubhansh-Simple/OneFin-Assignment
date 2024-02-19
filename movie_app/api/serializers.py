# movie_app/api/serializers.py

# django
from django.conf import settings

# rest_framework
from rest_framework import serializers

# local
from movie_app.models import Collections, Genres, Movies


# GENRES SERIALIZER
class GenreSerializer( serializers.ModelSerializer ):
    class Meta:
        model = Genres
        field = '__all__'


# MOVIES SERIALIZER
class MovieSerializer(serializers.ModelSerializer):
    #genres = GenreSerializer(many=True)

    class Meta:
        model  = Movies
        fields = '__all__'


class GETCollectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Collections
        fields = ['title','uuid','description']


# COLLECTIONS SERIALIZER
class GETRetrieveCollectionSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True, read_only=True)

    class Meta:
        model   = Collections
        fields  = ['title','description','movies']

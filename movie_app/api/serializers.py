# movie_app/api/serializers.py

# django
from django.conf import settings

# rest_framework
from rest_framework import serializers

# local
from movie_app.models import Collections, Genres, Movies


# GENRE SERIALIZER
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = '__all__'
        extra_kwargs = {
            'genres': {
                'validators': [],
            }
        }


# MOVIE SERIALIZER
class MovieSerializer(serializers.ModelSerializer):

    genres = GenreSerializer(many=True)

    class Meta:
        model  = Movies
        fields = '__all__'
        extra_kwargs = {
            'uuid': {
                'validators': [],
            }
        }


# COLLECTION LIST SERIALIZER
class CollectionListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Collections
        fields = ['title','uuid','description']


# COLLECTION RETRIEVE SERIALIZER
class CollectionDetailSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True, read_only=True)

    class Meta:
        model   = Collections
        fields  = ['title','description','movies']


# COLLECTION CREATE SERIALIZER
class CollectionCreateSerializer(serializers.ModelSerializer):

    creator = serializers.ReadOnlyField()
    movies  = MovieSerializer(many=True)

    class Meta:
        model  = Collections
        fields = ['title','description','creator','movies' ]

    # Custom Validators
    def run_validators(self, attrs):
        '''Generating the error messages as errors occured'''

        # SKIP validation for PUT request ( optional field )
        if self.partial: return attrs

        errors = {}
        if not attrs.get('title'):
            errors['title'] = 'Title is required'
        if not attrs.get('description'):
            errors['description'] = 'Description is required'
        if not attrs.get('movies'):
            errors['movies'] = 'Movies are required'

        if attrs.get('movies'):
            movies_list = attrs.get('movies')

            # Validate Data in Each Movie Record of Payload
            for movie in movies_list:
                single_error = {}
                if not movie.get('title'):
                    single_error['title'] = 'Title is required'
                if not movie.get('description'):
                    single_error['description'] = 'Description is required'
                if not movie.get('genres'):
                    single_error['genres'] = 'Genres is required'

                if single_error:
                    if errors.get('movies'):
                        errors['movies'].append(single_error)
                    else:
                        errors['movies'] = [single_error]
        
        if errors:
            raise serializers.ValidationError(errors)
        return attrs


    def create(self, validated_data):
        movies_list    = validated_data.pop('movies')
        all_movies     = handling_movies_and_genres(movies_list)
        collection_obj = Collections.objects.create(**validated_data)
        collection_obj.movies.set(all_movies)
        return collection_obj


def handling_movies_and_genres(movies_list):

    print('\nYOU ARE HERE\n')
    all_movies = []
    for movie in movies_list:
        all_genres = []
        genres_data = movie.pop('genres')
        for each_genres in genres_data:
            obj, created = Genres.objects.get_or_create(**each_genres)
            all_genres.append(obj)
        obj, created = Movies.objects.get_or_create(**movie)
        obj.genres.set(all_genres)
        obj.save()
        all_movies.append(obj)
    return all_movies


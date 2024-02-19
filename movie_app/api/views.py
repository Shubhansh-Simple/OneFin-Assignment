# movie_app/api/views.py

# python
from random      import randint
from collections import Counter
import requests
import time

# django
from django.conf      import settings
from django.db.models import Count

# rest_framework
from rest_framework             import status, viewsets
from rest_framework.views       import APIView
from rest_framework.response    import Response
from rest_framework.permissions import IsAuthenticated

# local
from movie_app.models import Collections, Genres, Movies
from movie_app.utils  import get_top_genres
from .permissions     import IsCollectionCreatorLoggedIn
from .serializers     import GETRetrieveCollectionSerializer, POSTPUTCollectionSerializer, GETCollectionSerializer


class MovieApiView( APIView ):
    '''Integrate 3rd party API with built-in retry mechanism'''

    def fetch_movies(self):
        url      = settings.MOVIE_API_URL
        username = settings.MOVIE_API_USERNAME 
        password = settings.MOVIE_API_PASSWORD
        response = requests.get(url, auth=(username,password))
        return response

    def get(self, request, format=None):

        max_retries = 3 
        min_delay, max_delay = 1, 5

        for _ in range(max_retries):
            try:
                response = self.fetch_movies()
                print('Response - ',response.status_code)

                if response.status_code == 200:
                    return Response( response.json(), status=response.status_code )
                else:
                    print('GET /movies/ FAILED!, Retrying ')
                    print('Response - ',response.text)
                    time.sleep( randint(min_delay, max_delay) )

            except requests.exceptions.RequestException as e:
                print('Request failed! (Retrying...), ',str(e))
                time.sleep( randint(min_delay, max_delay) )

        # If all retries fails, returns response with status code 503
        return Response({'message' : 'All retries failed'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)


class CollectionViewSet( viewsets.ViewSet ):
    serializer_class   = GETCollectionSerializer
    #permission_classes = [IsAuthenticated, IsCollectionCreatorLoggedIn]


    def list(self, request):
        #data       = Collections.objects.filter(creator=request.user)
        user_collections = Collections.objects.filter(creator_id=6)
        serializer       = GETCollectionSerializer(user_collections, many=True)

        # Get TOP 3 favourite genres
        user_movies = Movies.objects.filter(collections__in=user_collections)
        user_genres = Genres.objects.filter(movies__in=user_movies)

        queryset         = user_genres.values_list('genre_name',flat=True)
        favourite_genres = get_top_genres(queryset)

        response   = {
            'is_success' : True,
            'data' : {
                'collections' : serializer.data
                },
            'favourite_genres' : favourite_genres
        }
        return Response(response)



    def retrieve(self, request, pk=None):
        try:
            user_collection = Collections.objects.get(uuid=pk)
            serializer      = GETRetrieveCollectionSerializer(user_collection)

        except Collections.DoesNotExist:
            return Response({"error": "Object not found"}, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.data)

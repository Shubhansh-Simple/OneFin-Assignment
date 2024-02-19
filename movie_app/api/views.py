# movie_app/api/views.py

# python
from random import randint
import requests
import time

# 3rd Party
import uuid

# django
from django.conf         import settings
from django.contrib.auth import get_user_model

# rest_framework
from rest_framework             import status, viewsets
from rest_framework.views       import APIView
from rest_framework.response    import Response
from rest_framework.permissions import IsAuthenticated

# local
from movie_app.models import Collections, Genres, Movies
from movie_app.utils  import get_top_genres, prepare_response
from .permissions     import IsCollectionCreatorLoggedIn
from .serializers     import CollectionCreateSerializer, CollectionDetailSerializer, CollectionListSerializer 


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
                    print('Request failed! (Retrying...)')
                    print('Response - ',response.text)
                    time.sleep( randint(min_delay, max_delay) )

            except requests.exceptions.RequestException as e:
                print('Request failed! (Retrying...), ',str(e))
                time.sleep( randint(min_delay, max_delay) )

        # If all retries fails, returns response with status code 503
        return Response({'message' : 'All retries failed'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)


class CollectionViewSet( viewsets.ViewSet ):
    '''Implementing CRUD operations for Collections'''

    serializer_class   = CollectionCreateSerializer
    #permission_classes = [IsAuthenticated, IsCollectionCreatorLoggedIn]

    def list(self, request):
        #data       = Collections.objects.filter(creator=request.user)
        user_collections = Collections.objects.filter(creator_id=8)
        serializer       = CollectionListSerializer(user_collections, many=True)

        # CALCULATING TOP 3 GENRES
        user_movies = Movies.objects.filter(collections__in=user_collections)
        user_genres = Genres.objects.filter(movies__in=user_movies)

        queryset         = user_genres.values_list('genres',flat=True)
        favourite_genres = get_top_genres(queryset)

        response = prepare_response(serializer.data ,favourite_genres)
        return Response(response)


    def retrieve(self, request, pk=None):
        try:
            # Verify UUID
            uuid_obj = uuid.UUID(pk)

            user_collection = Collections.objects.get(uuid=pk)
            serializer      = CollectionDetailSerializer(user_collection)

        # Handle Invalid UUID
        except ValueError:
            response = {'error' : f'{pk} is not a valid UUID'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        # Handle No data found
        except Collections.DoesNotExist:
            response = {'error' : 'Object not found'}
            return Response(response, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.data)


    def create(self, request):
        user = get_user_model().objects.get(id=6)

        request_data = request.data.copy()
        request_data['creator'] = user #request.user.id  
        print('Requested data - ',request_data)

        serializer = CollectionCreateSerializer(data=request_data)

        if serializer.is_valid():
            print('It is valid')
            instance = serializer.save(creator=request_data['creator'])
            response = {'collection_uuid' : instance.uuid}
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        else:
            print('I am the ghost in your application')
            print(serializer.errors)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk=None):
        try:
            data = Collections.objects.get(uuid=pk)
            data.delete()
            response = {'message' : 'Deleted Successfully'}
            return Response(response, status=status.HTTP_200_OK)
        except:
            response = {'message' :  'No collection found'}

        return Response(response, status=status.HTTP_204_NO_CONTENT)





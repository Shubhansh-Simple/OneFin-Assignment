# movie_app/api/views.py

# python
from random import randint
import requests
import time

# django
from django.conf import settings

# rest_framework
from rest_framework          import status
from rest_framework.views    import APIView
from rest_framework.response import Response



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




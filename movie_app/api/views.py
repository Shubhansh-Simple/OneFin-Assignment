# movie_app/api/views.py

# python
import requests
import time

# django
from django.conf import settings

# rest_framework
from rest_framework          import status
from rest_framework.views    import APIView
from rest_framework.response import Response



class MovieApiView( APIView ):

    def fetch_movies(self):
        '''Retrieve the movies from 3rd party api'''

        url      = settings.MOVIE_API_URL
        username = settings.MOVIE_API_USERNAME 
        password = settings.MOVIE_API_PASSWORD
        response   = requests.get(url, auth=(username,password))
        return response


    def get(self, request, format=None):
        '''Return response with Handle exception and retrying request'''

        max_retries = 3 
        retry_delay = 2 # in seconds

        for _ in range(max_retries):
            try:
                response = self.fetch_movies()
                print('Response - ',response.status_code)

                if response.status_code == 200:
                    return Response( response.json(), status=response.status_code )
                else:
                    print('GET /movies/ FAILED!, Retrying ')
                    print('Response - ',response.text)
                    time.sleep(retry_delay)

            except requests.exceptions.RequestException as e:
                print('Request failed! (Retrying...), ',str(e))
                time.sleep(retry_delay)

        # If all retries fails, returns response with status code 503
        return Response({'message' : 'All retries failed'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)




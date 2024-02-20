# movie_app/tests.py

# django
from django.urls import reverse

# 3rd party
import uuid

# rest_framework
from rest_framework      import status
from rest_framework.test import APITestCase


class CollectionViewSetTest(APITestCase):

    # Get the URL for the CollectionViewSet
    base_url = reverse('collection-list')

    def test_create_collection_with_movies(self):
        """Failure Case: Server Collection Create Endpoint Not Implemented Successfully"""

        # Get the URL for the RegisterApiView
        token_url    = reverse('register')

        payload_data = {
                'username' : 'testuser', 
                'password' : '123456' 
        }

        # GET TOKEN
        jwt_response = self.client.post(token_url, data=payload_data, format='json')
        
        actual_status_code   = jwt_response.status_code
        expected_status_code = status.HTTP_200_OK

        self.assertEqual(
                actual_status_code,
                expected_status_code, 
                f'Expected status code {expected_status_code}, but got {actual_status_code}'
        )

        auth_header = f'Bearer {jwt_response.data["access_token"]}'

        collection_payload = {
            "title": "Science Fiction Movies",
            "description" : "My favourite movies of all times",
            "movies": [
                {
                    "title": "Inception",
                    "description": "A thief stole secrets by entering your dreams",
                    "genres": [ {"genres" : "Adventure"}, {"genres" : "Suspense"} ],
                    "uuid": "4802ed90-7129-4d53-919f-35c8974b47e6"
                }
            ]
        }

        # POST COLLECTION CREATE
        response = self.client.post( self.base_url, data=collection_payload, HTTP_AUTHORIZATION=auth_header, format='json' )

        actual_status_code   = response.status_code
        expected_status_code = status.HTTP_201_CREATED

        self.assertEqual(
                actual_status_code,
                expected_status_code, 
                f'Expected status code {expected_status_code}, but got {actual_status_code}'
        )
        data = response.data

        # Assert that the key 'collection_uuid' exists in the response data dictionary
        self.assertIn('collection_uuid',data)

        # Asserting that the 'collection_uuid' in the response data is an instance of UUID
        self.assertIsInstance(data['collection_uuid'], uuid.UUID)




# request_counter/tests.py

# django
from django.urls import reverse

# rest_framework
from rest_framework      import status
from rest_framework.test import APITestCase

class RequestCountApiViewTest(APITestCase):

    # Get the URL for the RequestCountApiView
    base_url      = reverse('request-count')

    def test_authentication_failure_without_token(self):
        """Failure Case: Server Authentication Endpoints Not Implemented Successfully"""

        # Make a GET request to the endpoint
        response = self.client.get(self.base_url)

        # Check that status code is 401 Unauthorized
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED, f'Expected status code 401, but got {response.status_code}')


    def test_authentication_success_with_token(self):
        """Failure Case: Unable to Access /request-count Endpoint Due to Lack of Active Access Token"""

        # Get the URL for the RegisterApiView
        token_url = reverse('register')

        payload_data = {
                'username' : 'testuser',
                'password' : '123456'
        }

        jwt_response = self.client.post(token_url, data=payload_data, format='json')

        # Check that status code is 200 OK
        self.assertEqual(jwt_response.status_code, status.HTTP_200_OK, f'Expected status code 200, but got {jwt_response.status_code}')

        auth_header = f'Bearer {jwt_response.data["access_token"]}'
        response    = self.client.get(self.base_url, HTTP_AUTHORIZATION=auth_header)

        # Check that status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK, f'Expected status code 200, but got {response.status_code}')

        # Assert that the key 'requests' exists in the response data dictionary
        self.assertIn('requests',response.data)





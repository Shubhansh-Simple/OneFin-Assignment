# request_counter/tests.py

# django
from django.urls import reverse

# rest_framework
from rest_framework      import status
from rest_framework.test import APITestCase

class RequestCountApiViewTest(APITestCase):

    def test_authentication_failure_without_token(self):
        """Test that accessing the protected routes without authentication token returns HTTP_401_UNAUTHORIZED"""

        # Get the URL for the RequestCountApiView
        url      = reverse('request-count')

        # Make a GET request to the endpoint
        response = self.client.get(url)

        # Check that status code is 401 Unauthorized
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED, f'Expected status code 401, but got {response.status_code}')



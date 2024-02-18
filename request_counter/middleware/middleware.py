# request_counter/middleware/middleware.py

from ..models import RequestCount

class RequestCounterMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        '''Increment request count'''

        print('You calling this middleware')

        request_count, created = RequestCount.objects.get_or_create(id=1)
        request_count.total_requests += 1
        request_count.save()

        # Call the next middleware or view
        response = self.get_response(request)
        return response

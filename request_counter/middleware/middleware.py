# request_counter/middleware/middleware.py

from django.db        import transaction
from django.db.models import F
from request_counter.models import RequestCount

class RequestCounterMiddleware:
    '''Customer middleware for counting all requests coming to server'''

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        '''Increment request count'''

        # Work with MODERATE level of concurrency ( Since using SQLITE )
        with transaction.atomic():
            request_count = RequestCount.objects.select_for_update().get_or_create(id=1)[0]
            request_count.total_requests = F('total_requests') + 1
            request_count.save()

        # Call the next middleware or view
        response = self.get_response(request)
        return response



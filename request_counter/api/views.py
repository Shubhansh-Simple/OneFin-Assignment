from rest_framework          import generics
from rest_framework.response import Response

# local
from request_counter.models  import RequestCount
from .serializers            import RequestCountSerializer


class RequestCountDetailApiView( generics.RetrieveAPIView ):
    '''Return total requests servered by the server'''

    queryset         = RequestCount.objects.all()
    serializer_class = RequestCountSerializer

    def get_object(self):
        '''Get first item from records'''

        queryset = self.filter_queryset( self.get_queryset() )
        obj      = queryset.first()
        return obj


class RequestCounterUpdateApiView( generics.UpdateAPIView ):
    '''Reset total requests servered by the server'''

    queryset         = RequestCount.objects.first()
    serializer_class = RequestCountSerializer

    def get_object(self):
        '''Get first item from records'''

        obj = self.filter_queryset( self.get_queryset() )
        return obj


    def perform_update(self, serializer):
        '''Reset the total request value to 0'''

        serializer.instance.total_requests = 0
        serializer.save()
        return Response({'message' : 'request count reset successfully'})




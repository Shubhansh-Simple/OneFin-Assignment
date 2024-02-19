# request_counter/api/views.py

# rest_framework
from rest_framework          import status
from rest_framework.views    import APIView
from rest_framework.response import Response

# local
from request_counter.models  import RequestCount
from .serializers            import RequestCountSerializer


class RequestCountApiView( APIView ):
    '''Return total requests servered by the server'''

    def get(self,request,format=None):

        obj        = RequestCount.objects.first()
        serializer = RequestCountSerializer(obj)

        return Response( serializer.data, status=status.HTTP_200_OK )


class ResetRequestCountApiView( APIView ):
    '''Reset total requests servered by the server in database'''

    def post(self,request,format=None):

        obj      = RequestCount.objects.first()
        if obj:
            obj.total_requests = 0
            obj.save()
        response = { 'message': 'request count reset successfully' }

        return Response( response, status=status.HTTP_200_OK )


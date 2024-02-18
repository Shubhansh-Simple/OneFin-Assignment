from rest_framework import serializers
from ..models       import RequestCount

class RequestCountSerializer( serializers.ModelSerializer ):

    requests = serializers.SerializerMethodField()

    class Meta:
        model  = RequestCount
        fields = ('requests',)
        read_only_fields = ('requests',)

    def get_requests(self,obj):
        '''Overriding name in JSON'''

        return obj.total_requests



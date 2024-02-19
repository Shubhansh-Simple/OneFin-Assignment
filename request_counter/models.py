# request_counter/models.py

# django
from django.db import models

class RequestCount(models.Model):
    '''Request Count Tracking Table'''

    total_requests = models.PositiveIntegerField( default=0, 
                                                  verbose_name='Total requests servered by the server' )

    def __str__(self):
        return f'Total servered requests - {self.total_requests}'



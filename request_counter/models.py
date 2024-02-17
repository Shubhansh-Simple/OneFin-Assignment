from django.db import models

class RequestCount(models.Model):
    total_requests = models.PositiveIntegerField( default=0, 
                                                  verbose_name='Total number of requests which have been served by the server' )

    def __str__(self):
        return f'Total servered requests - {self.total_requests}'



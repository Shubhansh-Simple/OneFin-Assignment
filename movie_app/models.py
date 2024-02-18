# movie_app/models.py

# django
from django.db   import models
from django.conf import settings 


# Movie's Genres
class Genres(models.Model):
    '''Table for genres of movies'''

    genre_name = models.CharField( primary_key=True, max_length=100 )

    class Meta:
        verbose_name        = 'Genres'
        verbose_name_plural = 'Genres'

    def __str__(self):
        return f'Genres - {self.genre_name.title()}'


class Movies(models.Model):
    class Meta:
        verbose_name        = 'Movie'
        verbose_name_plural = 'Movies'

    title       = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    genres      = models.ManyToManyField(Genres, null=True)
    uuid        = models.UUIDField(primary_key=True)

    def __str__(self):
        return f'Movie - {self.title.title()}'



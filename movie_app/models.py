# movie_app/models.py

# django
from django.db   import models
from django.conf import settings 

# third party
import uuid


# Movie's Genres
class Genres(models.Model):
    genres = models.CharField( primary_key=True, max_length=100 )

    class Meta:
        verbose_name        = 'Genres'
        verbose_name_plural = 'Genres'

    def __str__(self):
        return f'{self.genres.title()}'


# Movie's Table
class Movies(models.Model):

    class Meta:
        verbose_name        = 'Movie'
        verbose_name_plural = 'Movies'

    uuid        = models.UUIDField(primary_key=True)
    title       = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    genres      = models.ManyToManyField(Genres, related_name='movies', blank=True)

    def __str__(self):
        return f'Movie - {self.title.title()}'

# Collection's Table
class Collections(models.Model):

    class Meta:
        verbose_name        = 'Collection'
        verbose_name_plural = 'Collections'

    uuid        = models.UUIDField(primary_key=True, default=uuid.uuid4 )
    title       = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    movies      = models.ManyToManyField(Movies, related_name='collections', blank=True)
    creator     = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.creator.username}'s Collection - {self.title}"


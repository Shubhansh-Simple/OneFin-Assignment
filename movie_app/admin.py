# movie_app/admin.py

# django
from django.contrib import admin

# local
from .models        import Movies, Genres, Collections

# register models for Admin site
admin.site.register(Movies)
admin.site.register(Genres)
admin.site.register(Collections)



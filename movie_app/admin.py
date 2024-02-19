from django.contrib import admin
from .models        import Movies, Genres, Collections

admin.site.register(Movies)
admin.site.register(Genres)
admin.site.register(Collections)



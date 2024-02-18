# movie_app/api/urls.py

from django.urls import path
from .views      import MovieApiView

urlpatterns = [
    path('movies/', MovieApiView.as_view() ),
]

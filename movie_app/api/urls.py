# movie_app/api/urls.py

# django
from django.urls import path

# rest_framework
from rest_framework.routers import DefaultRouter

# local
from .views import MovieApiView, CollectionViewSet

urlpatterns = [
    path('movies/', MovieApiView.as_view(), name='movie-list' ),
]

# Default Router
router = DefaultRouter()
router.register(r'collection', CollectionViewSet, basename='collection')

# Add to parent urls
urlpatterns += router.urls

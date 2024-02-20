# users/api/urls.py

# django 
from django.urls import path

# local
from .views import RegisterApi

urlpatterns = [
    path('', RegisterApi.as_view(), name='register' ),
]


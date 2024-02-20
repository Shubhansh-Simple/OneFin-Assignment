# users/api/urls.py

# django 
from django.urls import path

# local
from .views import RegisterApiView

urlpatterns = [
    path('', RegisterApiView.as_view(), name='register' ),
]


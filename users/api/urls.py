# users/api/urls.py

# django 
from django.urls import path

# rest_framework
from rest_framework_simplejwt import views as jwt_view

# local
from .views import RegisterApi


urlpatterns = [
    path('register/', RegisterApi.as_view() ),
    path('login/', jwt_view.TokenObtainPairView.as_view(), name='token_obtain' ),
]


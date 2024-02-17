from django.urls import path
from .views      import RequestCountDetailApiView, RequestCounterUpdateApiView

urlpatterns = [
    path('',       RequestCountDetailApiView.as_view() ),
    path('reset/', RequestCounterUpdateApiView.as_view() ),
]

# request_counter/api/urls.py

# django
from django.urls import path
from .views      import RequestCountApiView, ResetRequestCountApiView

urlpatterns = [
    path('',       RequestCountApiView.as_view(),      name='request-count'),
    path('reset/', ResetRequestCountApiView.as_view(), name='request-count-reset'),
]

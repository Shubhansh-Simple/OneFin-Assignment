# config/urls.py

# django
from django.contrib import admin
from django.urls    import path,include

urlpatterns = [
    # For admin site
    path('admin/', admin.site.urls),
    # Movies & Collections
    path('',          include('movie_app.api.urls')),
    # Register for JWT token
    path('register/', include('users.api.urls') ),
    # Request count
    path('request-count/', include('request_counter.api.urls') ),
]

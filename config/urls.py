# config/urls.py

# django
from django.contrib import admin
from django.urls    import path,include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('movie_app.api.urls')),
    path('register/', include('users.api.urls') ),
    path('request-count/', include('request_counter.api.urls') ),
]

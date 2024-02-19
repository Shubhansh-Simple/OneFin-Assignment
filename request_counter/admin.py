# request_counter/admin.py

#django
from django.contrib import admin
from .models        import RequestCount

# register model for Admin site
admin.site.register(RequestCount)

# users/admin.py

# django
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin

# local
from .models        import CustomUser

class CustomUserAdmin(UserAdmin):
    pass

admin.site.register(CustomUser, CustomUserAdmin)


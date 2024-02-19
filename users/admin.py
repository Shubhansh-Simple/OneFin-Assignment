# users/admin.py

# django
from django.contrib.auth.admin import UserAdmin
from django.contrib            import admin

# local
from .models        import CustomUser

class CustomUserAdmin(UserAdmin):
    '''Register CustomerUser model in admin site'''
    pass

# register model for Admin site
admin.site.register(CustomUser, CustomUserAdmin)


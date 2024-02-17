from django.contrib.auth.models import AbstractUser
from django.db                  import models

class CustomUser( AbstractUser ):
    '''Override the existing user table created by Django'''

    class Meta:
        db_table            = 'users_customuser'
        verbose_name        = 'Account'
        verbose_name_plural = 'Accounts'
    
    def __str__(self):
        return 'User - '+str(self.username).capitalize()


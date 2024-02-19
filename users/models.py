# users/models.py

from django.contrib.auth.models import AbstractUser

class CustomUser( AbstractUser ):
    '''Override the existing user table created by Django'''

    class Meta:
        db_table            = 'users_customuser'
        verbose_name        = 'Account'
        verbose_name_plural = 'Accounts'

    '''
    Can add more fields in existing table, if required
    '''
    
    def __str__(self):
        return 'User - '+str(self.username).capitalize()


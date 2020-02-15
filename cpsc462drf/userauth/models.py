from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(
        db_index=True, max_length=255, unique=True)

    REQUIRED_FIELDS = ['email']
    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'

    def get_username(self):
        return self.username

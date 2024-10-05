"""
# app/core/models.py

Models for Django Application
"""

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)


class UserManager(BaseUserManager):
    """Manager class for User Model."""

    def create_user(self, email, password=None, **extra_fields):
        """This methods create a new user in the system."""
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Appending User Model for added functionalities."""
    email = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    # Create the user
    objects = UserManager()

    REQUIRED_FIELDS = []

    # Overriding in system to use 'email' instead of
    # username when authenticating
    USERNAME_FIELD = 'email'
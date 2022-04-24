from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings


class UserProfileManager(BaseUserManager):
    """Manager for user profile"""

    def create_user(self, email, name, password=None):
        """"Create new User"""

        if not email:
            raise ValueError('User should have an email')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        """Create superuser"""

        user = self.create_user(email, name, password)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Base Model for system User"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def __str__(self):
        return self.email


class ProfileFeedItem(models.Model):
    """Profile status update"""

    user_profile = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status_text = models.CharField(max_length=255)
    created_on = models.DateField(auto_now=True)

    def __str__(self):
        return self.status_text

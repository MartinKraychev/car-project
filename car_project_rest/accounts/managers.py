from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.db import models


class CustomManager(models.Manager):
    """
    Manager that returns not deleted items
    """

    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)


class SoftDeletedManager(models.Manager):
    """
    Manager that returns only deleted items
    """
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=False)


class CustomUserManager(BaseUserManager):
    def _create_user(self, username, email, date_of_birth, gender, password, **extra_fields):
        """
        Create and save a user with the given username, email, date of birth, gender and password.
        """
        if not username:
            raise ValueError("The given username must be set")
        email = self.normalize_email(email)

        user = self.model(username=username, email=email, date_of_birth=date_of_birth, gender=gender, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, date_of_birth=None, gender=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, email, date_of_birth, gender, password, **extra_fields)

    def create_superuser(self, username, email=None, date_of_birth=None, gender=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(username, email, date_of_birth, gender, password, **extra_fields)

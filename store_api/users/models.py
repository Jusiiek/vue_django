import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, email, password, is_global_user=False, is_active=True, is_superuser=False, is_staff=False):
        if not email:
            raise ValueError("Users must have an email address")
        if not password:
            raise ValueError("Users must have a password")

        user = self.model(
            email=self.normalize_email(email),
            is_global_user=is_global_user,
            is_active=is_active,
            is_superuser=is_superuser,
            is_staff=is_staff
        )
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        return self.create_user(email=email, password=password, is_global_user=False, is_active=True, is_superuser=True, is_staff=True)


# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    username = models.CharField(default="", max_length=128)

    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    is_global_user = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

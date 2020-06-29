from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from django.core.exceptions import ValidationError
from django.db import models


# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, phone, password=None):
        """
        Creates and saves a User with the given phone and password.
        """
        if not phone:
            raise ValueError('Users must have a  phone number')

        user = self.model(
            phone=self.normalize_userid(phone),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password):
        """
        Creates and saves a superuser with the given phone and password.
        """
        user = self.create_user(
            phone,
            password=password,
        )
        user.save(using=self._db)
        return user


class UserRegistration(AbstractBaseUser):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=200, unique=True, verbose_name='email address')
    phone = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=150)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []
    objects = UserManager()

from pizza_lab.accounts.managers import AppUserManager
from django.contrib.auth import models as auth_models
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class CustomUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    USERNAME_FIELD = 'email'
    EMAIL_VERBOSE_NAME = 'Email'
    EMAIL_MAX_LENGTH = 100
    IS_STAFF_VERBOSE_NAME = 'Employee'
    IS_ACTIVE_VERBOSE_NAME = 'Active user'
    DATE_JOINED_VERBOSE_NAME = 'Date joined'

    email = models.EmailField(
        verbose_name=EMAIL_VERBOSE_NAME,
        max_length=EMAIL_MAX_LENGTH,
        unique=True,
        null=False,
        blank=False,
    )

    is_staff = models.BooleanField(
        verbose_name=IS_STAFF_VERBOSE_NAME,
        default=False,
        null=False,
        blank=False
    )

    is_active = models.BooleanField(
        verbose_name=IS_ACTIVE_VERBOSE_NAME,
        default=True,
        null=False,
        blank=False,
    )

    date_joined = models.DateField(
        verbose_name=DATE_JOINED_VERBOSE_NAME,
        auto_now_add=True
    )

    objects = AppUserManager()

    def __str__(self):
        return self.email


class Profile(models.Model):
    FIRST_NAME_VERBOSE_NAME = 'First name'
    FIRST_NAME_MAX_LEN = 30
    LAST_NAME_VERBOSE_NAME = 'Last name'
    LAST_NAME_MAX_LEN = 30

    first_name = models.CharField(
        verbose_name=FIRST_NAME_VERBOSE_NAME,
        max_length=FIRST_NAME_MAX_LEN,
        null=False,
        blank=False
    )
    last_name = models.CharField(
        verbose_name=LAST_NAME_VERBOSE_NAME,
        max_length=LAST_NAME_MAX_LEN,
        null=False,
        blank=False
    )

    user = models.OneToOneField(
        CustomUser,
        primary_key=True,
        on_delete=models.CASCADE,
    )

    def get_full_name(self):
        full_name = f'{self.first_name} {self.last_name}'
        return full_name

    def get_short_name(self):
        return self.first_name

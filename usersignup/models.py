from django.core import validators
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# Create your models here.
from common_definations.validators import mobile_number_validator
from common_definations.validators import name_validator
from django.utils.translation import gettext_lazy as _


class User(AbstractBaseUser, PermissionsMixin):

    first_name = models.CharField(max_length=100, blank=False, validators=[
        name_validator])
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=False, null=False, unique=True)
    mobile_no = models.CharField(
        max_length=10, unique=True, blank=False, null=False, validators=[mobile_number_validator])
    dob = models.DateField(null=False, blank=False)
    register_date = models.DateTimeField(
        auto_created=True, auto_now_add=True, blank=False)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'mobile_no'

    def __str__(self) -> str:
        return self.first_name

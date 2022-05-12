from django.utils.translation import gettext_lazy as _

from django.utils import timezone

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models

from car_project_rest.accounts.managers import CustomUserManager, CustomManager, SoftDeletedManager


class SoftDeleteModel(models.Model):
    """
    ABS model that all other models inherit.
    Has 2 different manager depending on the purpose.
    """
    deleted_at = models.DateTimeField(null=True, blank=True, default=None)
    objects = CustomManager()
    deleted_objects = SoftDeletedManager()

    def soft_delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        self.deleted_at = None
        self.save()

    class Meta:
        abstract = True


class CustomUser(AbstractBaseUser, PermissionsMixin, SoftDeleteModel):
    """
    Extended User Model
    """
    HELP_TEXT_USERNAME = "Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only."
    HELP_TEXT_IS_STAFF = "Designates whether the user can log into this admin site."
    ERROR_MSG_UNIQUE_USERNAME = "A user with that username already exists."

    USERNAME_MAX_LENGTH = 30
    GENDERS = ['Male', 'Female', 'Other']
    GENDER_CHOICES = [(g, g) for g in GENDERS]

    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _("username"),
        max_length=USERNAME_MAX_LENGTH,
        unique=True,
        help_text=_(
            HELP_TEXT_USERNAME
        ),
        validators=[username_validator],
        error_messages={
            "unique": _(ERROR_MSG_UNIQUE_USERNAME),
        },
    )

    email = models.EmailField(_("email address"), blank=True)
    date_of_birth = models.DateField(_("date of birth"), blank=True, null=True)
    gender = models.CharField(
        _("gender choice"),
        max_length=max(len(x) for x in GENDERS),
        choices=GENDER_CHOICES,
        blank=True,
        null=True,
    )

    date_joined = models.DateTimeField(
        _("date joined"),
        default=timezone.now,
    )

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_(HELP_TEXT_IS_STAFF),
    )

    def __str__(self):
        return f'{self.username}'

    USERNAME_FIELD = 'username'

    objects = CustomUserManager()

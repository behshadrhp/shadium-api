import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from apps.account.managers.custom_user_manager import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    """
    This class is for Set User model.
    """
    
    # id model
    pkid = models.BigAutoField(primary_key=True, editable=False, unique=True)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    # initial info
    email = models.EmailField(db_index=True, unique=True)

    # permissions
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # created time
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"
    
    objects = CustomUserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.email
    
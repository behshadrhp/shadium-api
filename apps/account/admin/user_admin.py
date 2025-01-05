from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from apps.account.forms.user_admin_form import UserCreationForm, UserChangeForm

User = get_user_model()


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """
    The UserAdmin class is for creating and displaying users and can be managed from this section.
    """
    
    list_display = ["pkid", "email", "first_name", "last_name", "is_active", "is_staff", "is_superuser", "date_joined"]
    list_filter = ["is_active", "is_staff", "is_superuser", "date_joined"]
    list_display_links = ["pkid", "email", "first_name", "last_name"]

    search_fields = ["email__icontains", "first_name__icontains", "last_name__icontains"]
    ordering = ["is_superuser", "is_staff", "-date_joined"]
    readonly_fields = ["last_login", "date_joined"]
    list_per_page = 10

    form = UserChangeForm
    add_form = UserCreationForm
    model = User

    fieldsets = (
        (_("Login Credentials"), {"fields": ("email", "password")}),
        (_("Personal Info"), {"fields": ("first_name", "last_name")}),
        (_("Permissions and Groups"), {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        (_("Important Date"), {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "first_name", "last_name", "password1", "password2"),
            },
        ),
    )

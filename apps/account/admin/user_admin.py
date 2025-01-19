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
    
    list_display = ["pkid", "email", "is_active", "is_staff", "is_superuser", "date_joined"]
    list_filter = ["is_active", "is_staff", "is_superuser", "date_joined"]
    list_display_links = ["pkid", "email"]

    search_fields = ["email__icontains"]
    ordering = ["is_superuser", "is_staff", "-date_joined"]
    readonly_fields = ["last_login", "date_joined"]
    list_per_page = 10

    form = UserChangeForm
    add_form = UserCreationForm
    model = User

    fieldsets = (
        (_("Login Credentials"), {"fields": ("email", "password")}),
        (_("Permissions and Groups"), {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        (_("Important Date"), {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )

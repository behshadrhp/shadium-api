from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

User = get_user_model()

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """
    The UserAdmin class is for creating and displaying users and can be managed from this section.
    """ 

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
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

    list_display = ["email", "first_name", "last_name", "is_active","is_staff", "is_superuser", "formatted_date_joined", "formatted_last_login"]
    list_filter = ["is_staff", "is_superuser", "is_active", "groups", "date_joined", "last_login"]
    search_fields = ["email__icontains"]
    ordering = ["-is_superuser", "-is_staff", "-last_login"]
    list_per_page = 10
    readonly_fields = ["last_login", "date_joined"]

    @admin.display(description="Date joined")
    def formatted_date_joined(self, obj):
        return obj.date_joined.strftime("%Y-%m-%d") if obj.date_joined else None

    @admin.display(description="Last login")
    def formatted_last_login(self, obj):
        return obj.last_login.strftime("%Y-%m-%d") if obj.last_login else None
    
    def get_readonly_fields(self, request, obj=None):
        if obj: # if register new user
            return self.readonly_fields + ["email"]
        return self.readonly_fields

    def has_add_permission(self, request) -> bool:
          return request.user.is_superuser
    
    def has_delete_permission(self, request, obj=None) -> bool:
        # Permission Just for SuperUser
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None) -> bool:
        if request.user.is_superuser: # Checks User is Superuser access to change
             return True
        elif obj is not None and request.user.is_authenticated: # Checks whether the user is authenticated or not empty.
            if obj.email == request.user.email:
                return True
            elif obj.email is None and obj == request.user.email: # Checks if the user is the same person.
                return True
            else:
                return False
        return super().has_change_permission(request, obj)

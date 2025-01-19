from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from apps.account.models.profile_model import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """
    The Profile class is for creating and displaying users and can be managed from this section.
    """
    
    list_display = ["pkid", "user", "first_name", "last_name", "phone_number", "gender", "country", "created_at", "updated_at"]
    list_filter = ["gender", "country", "created_at", "updated_at"]
    list_display_links = ["pkid", "user", "first_name", "last_name", "phone_number"]

    search_fields = ["pkid__icontains", "user__email__icontains", "first_name__icontains", "last_name__icontains"]
    list_per_page = 10

    fieldsets = (
        (_("relationships"), {"fields": ("user", "followers")}),
        (_("initial information"), {"fields": ("avatar", "first_name", "last_name", "phone_number", "biography", "gender", "country", "city", "twitter")}),
    )

    def has_add_permission(self, request):
        return False
    
    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser
    
    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

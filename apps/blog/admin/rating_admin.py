from django.contrib import admin

from csvexport.actions import csvexport
from import_export.admin import ExportActionMixin 

from apps.blog.models.rating_model import Rating


@admin.register(Rating)
class RatingAdmin(ExportActionMixin, admin.ModelAdmin):
    """
    Monitoring all received Rating from users.
    """
    
    list_display = ["user", "post", "rating_type", "created_at", "updated_at"]
    list_display_links = ["user", "post"]
    list_filter = ["user", "post", "rating_type", "created_at", "updated_at"]
    search_fields = ["post__title__icontains", "post__body__icontains"]
    fields = ["user", "post", "rating_type", "description", "created_at", "updated_at"]
    readonly_fields = ["created_at", "updated_at"]
    ordering = ["created_at", "updated_at"]

    actions = [csvexport]
    
    def has_add_permission(self, request) -> bool:
        return request.user.is_staff
    
    def has_change_permission(self, request, obj=None) -> bool:
        return request.user.is_staff

    def has_delete_permission(self, request, obj=None) -> bool:
        return request.user.is_staff

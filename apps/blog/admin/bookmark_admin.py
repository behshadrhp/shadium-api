from django.contrib import admin

from csvexport.actions import csvexport
from import_export.admin import ExportActionMixin 

from apps.blog.models.bookmark_model import BookMark


@admin.register(BookMark)
class BookMarkAdmin(ExportActionMixin, admin.ModelAdmin):
    """
    Monitoring All user BookMark.
    save posts.
    """
    
    list_display = ["user", "post", "is_deleted", "created_at", "updated_at"]
    list_filter = ["user", "post", "is_deleted", "created_at", "updated_at"]
    search_fields = ["user__email__icontains", "post__title__icontains"]
    fields = [ "user", "post", "is_deleted", "created_at", "updated_at"]
    ordering = ["user", "post", "is_deleted", "created_at", "updated_at"]
    readonly_fields = ["created_at", "updated_at"]

    actions = [csvexport]
    
    def has_add_permission(self, request) -> bool:
        return request.user.is_staff
    
    def has_change_permission(self, request, obj=None) -> bool:
        return request.user.is_staff

    def has_delete_permission(self, request, obj=None) -> bool:
        return request.user.is_staff

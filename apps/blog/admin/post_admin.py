from django.contrib import admin

from csvexport.actions import csvexport
from markdownx.admin import MarkdownxModelAdmin
from import_export.admin import ExportActionMixin 

from apps.blog.models.post_model import Post, PostView


@admin.register(Post)
class PostAdmin(MarkdownxModelAdmin, ExportActionMixin, admin.ModelAdmin):
    """
    Monitoring Post on blog.
    """
    
    list_display = ["author", "title", "slug", "status", "study_time", "created_at", "updated_at"]
    list_display_links = ["author", "title", "slug"]
    list_filter = ["author", "status", "created_at", "updated_at"]
    search_fields = ["title__icontains", "body__icontains"]
    fields = ["cover", "title", "slug", "body", "status", "study_time", "tags"]
    readonly_fields = ["author", "slug", "study_time"]
    ordering = ["created_at", "updated_at", "status"]

    actions = [csvexport]
    
    def has_add_permission(self, request) -> bool:
        return request.user.is_staff
    
    def has_change_permission(self, request, obj=None) -> bool:
        if obj is None:
            return True  # Allow access to the change list
        # Only allow changes if the post belongs to the current user (author)
        return obj.author == request.user

    def has_delete_permission(self, request, obj=None) -> bool:
        return request.user.is_staff
    
    # save author
    def save_model(self, request, obj, form, change):
        # change author field to author requested
        obj.author = request.user
        return super().save_model(request, obj, form, change)


@admin.register(PostView)
class PostViewAdmin(MarkdownxModelAdmin, ExportActionMixin, admin.ModelAdmin):
    """
    Monitoring All Post View on blog.
    """
    
    list_display = ["post", "user", "visitor_ip", "created_at", "updated_at"]
    list_filter = ["post", "user", "visitor_ip", "created_at", "updated_at"]
    search_fields = ["visitor_ip__icontains", "user__email__icontains"]
    fields = ["post", "user", "visitor_ip", "created_at", "updated_at"]
    ordering = ["created_at", "updated_at"]

    actions = [csvexport]
    
    def has_add_permission(self, request) -> bool:
        return False
    
    def has_change_permission(self, request, obj=None) -> bool:
        return False

    def has_delete_permission(self, request, obj=None) -> bool:
        return request.user.is_staff

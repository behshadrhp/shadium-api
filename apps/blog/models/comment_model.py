from django.db import models
from django.contrib.auth import get_user_model

from core.models.base_model import BaseModel
from apps.blog.models.post_model import Post


User = get_user_model()

class Comment(BaseModel):

    # user & post & comment replay relations
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comment")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_comment")
    replay = models.ForeignKey("self", on_delete=models.CASCADE, related_name="replay_comment", null=True, blank=True)

    # message
    message = models.TextField()

    # settings
    is_deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        indexes = [
            models.Index(fields=["user", "post",]),
        ]
    
    def __str__(self):
        return f"{self.user.email} commented on {self.post.title}"

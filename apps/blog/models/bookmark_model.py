from django.db import models
from django.contrib.auth import get_user_model

from core.models.base_model import BaseModel

from apps.blog.models.post_model import Post


User = get_user_model()

class BookMark(BaseModel):

    # user and post relation
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_bookmark")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_bookmark")

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "BookMark"
        verbose_name_plural = "BookMarks"
        unique_together = ("user", "post")
        indexes = [
            models.Index(fields=["user", "post",]),
        ]

    def __str__(self):
        return f"{self.user.email} - {self.post.title}"

from django.db import models
from django.contrib.auth import get_user_model

from core.models.base_model import BaseModel
from apps.blog.models.post_model import Post

from utils.type.blog.rating_type import RatingType


User = get_user_model()

class Rating(BaseModel):

    # user & post relationship
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_rating")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_rating")

    # initial fields
    description = models.TextField(null=True, blank=True)

    # rating
    rating_type = models.CharField(max_length=10, choices=RatingType.choices)

    class Meta:
        ordering = ["-created_at"]
        unique_together = ("user", "post")
        verbose_name = "Rating"
        verbose_name_plural = "Ratings"
        indexes = [
            models.Index(fields=["user",]),
        ]
    
    def __str__(self):
        return f"{self.post.title} - {self.rating_type}"
    
from django.db import models
from django.db.models import Q
from django.contrib.auth import get_user_model

from autoslug import AutoSlugField
from tinymce.models import HTMLField
from taggit.managers import TaggableManager

from core.models.base_model import BaseModel

from utils.type.blog.post_status_type import PostStatus
from utils.tools.blog.read_time_engine import PostReadTimeEngine


User = get_user_model()


class Clap(BaseModel):

    # user and post relations
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_clap")
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="post_clap")

    # settings
    is_deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Clap"
        verbose_name_plural = "Claps"
        constraints = [
            models.UniqueConstraint(
                fields=["user", "post"],
                condition=Q(is_deleted=False),
                name="unique_active_clap"
            ),
        ]
        indexes = [
            models.Index(fields=["user", "post",]),
        ]

    def __str__(self):
        return f"{self.user.email} clapped {self.post.title}"
    

class Post(BaseModel):

    # user and tags and claps relations
    tags = TaggableManager(blank=True)
    claps = models.ManyToManyField(User, through=Clap, related_name="clapped_post")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author_blog_post")

    # information about post 
    cover = models.ImageField(upload_to="post/cover/", default="default/no-image.jpg")
    title = models.CharField(max_length=255, unique=True)
    slug = AutoSlugField(populate_from="title", always_update=True, unique=True)
    body = HTMLField()

    # post status -> is publish or draft
    status = models.CharField(max_length=2, choices=PostStatus.choices, default=PostStatus.PB)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        indexes = [
            models.Index(fields=["author",]),
        ]

    def __str__(self):
        return self.title
    
    @property
    def study_time(self):
        return PostReadTimeEngine.estimate_reading_time(self)


class PostView(BaseModel):

    # user and post relation
    post = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_post")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="user_post_view")

    # Registering visitor IPs
    visitor_ip = models.GenericIPAddressField(null=True, blank=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Post View"
        verbose_name_plural = "Post Views"
        unique_together = ("post", "user", "visitor_ip")
        indexes = [
            models.Index(fields=["post", "user",]),
        ]

    def __str__(self):
        return f"{self.post.title} viewed by {self.user.email if self.user else 'Anonymous'} from IP {self.visitor_ip}"
    
    @classmethod
    def record_view(cls, post, user, visitor_ip):
        post_view, _ = cls.objects.get_or_create(post=post, user=user, visitor_ip=visitor_ip)
        post_view.save()

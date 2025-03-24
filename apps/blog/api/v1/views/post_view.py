from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from apps.blog.models.post_model import Post
from apps.blog.api.v1.serializers.post_serializer import PostSerializer

from utils.type.blog.post_status_type import PostStatus


class PostExploreViewSet(ModelViewSet):

    queryset = Post.objects.select_related("author").all().filter(status=PostStatus.PB)
    serializer_class = PostSerializer
    http_method_names = ["get"]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = [
        "title__icontains", "author__user_profile__first_name__icontains", 
        "author__user_profile__last_name__icontains"
    ]
    lookup_field = "id"


class PostViewSet(ModelViewSet):

    serializer_class = PostSerializer
    http_method_names = ["get", "post", "put", "patch"]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = [
        "title__icontains", "author__user_profile__first_name__icontains", 
        "author__user_profile__last_name__icontains"
    ]
    lookup_field = "id"

    def get_queryset(self):
        return Post.objects.select_related("author").all().filter(author=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)
    
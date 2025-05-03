from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from apps.blog.models.comment_model import Comment
from apps.blog.api.v1.serializers.comment_serializer import GetCommentSerializer, PostCommentSerializer, PutCommentSerializer


class CommentViewSet(ModelViewSet):

    http_method_names = ["get", "post", "put", "patch"]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ["post__title__icontains"]
    lookup_field = "id"

    def get_queryset(self):
        user = self.request.user
        return Comment.objects.select_related("user", "post", "replay").all().filter(user=user, is_deleted=False)

    def get_serializer_class(self):
        if self.request.method == "GET":
            return GetCommentSerializer
        elif self.request.method == "POST":
            return PostCommentSerializer
        elif self.request.method == "PUT" or self.request.method == "PATCH":
            return PutCommentSerializer
    
    def perform_create(self, serializer):
        user = self.request.user
        return serializer.save(user=user)


class CommentExploreViewSet(ModelViewSet):

    queryset = Comment.objects.select_related("user", "post", "replay").all().filter(is_deleted=False)
    serializer_class = GetCommentSerializer
    http_method_names = ["get"]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ["post__title__icontains"]
    lookup_field = "id"

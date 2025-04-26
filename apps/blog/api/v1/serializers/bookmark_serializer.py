from rest_framework import serializers

from apps.blog.models.bookmark_model import BookMark

from apps.blog.api.v1.serializers.post_serializer import PostSerializer


class GetBookMarkSerializer(serializers.ModelSerializer):

    user = serializers.SerializerMethodField()
    post = PostSerializer(read_only=True)

    class Meta:
        model = BookMark
        fields = ["id", "user", "post", "is_deleted", "created_at", "updated_at"]

    def get_user(self, bookmark: BookMark):
        return bookmark.user.email


class PostBookMarkSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BookMark
        fields = ["post"]


class PutBookMarkSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookMark
        fields = ["is_deleted"]

from rest_framework import serializers

from apps.blog.models.comment_model import Comment

from apps.blog.api.v1.serializers.post_serializer import PostSerializer


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ["id", "user", "replay", "message", "is_deleted", "created_at", "updated_at"]

    def get_user(self, comment: Comment):
        return comment.user.email


class GetCommentSerializer(serializers.ModelSerializer):

    user = serializers.SerializerMethodField()
    post = PostSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "user", "post", "replay", "message", "is_deleted", "created_at", "updated_at"]

    def get_user(self, comment: Comment):
        return comment.user.email


class PostCommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = ["post", "replay", "message"]


class PutCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ["is_deleted"]

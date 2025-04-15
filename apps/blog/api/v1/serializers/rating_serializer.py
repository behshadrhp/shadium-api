from rest_framework import serializers

from apps.blog.models.rating_model import Rating
from apps.account.api.v1.serializers.user_serializer import UserSerializer


class RatingSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    post_id = serializers.IntegerField(source="post.id", read_only=True)
    post_title = serializers.CharField(source="post.title", read_only=True)

    class Meta:
        model = Rating
        fields = [
            "id", "user", "post_id", "post_title", 
            "rating_type", "description", "created_at"
        ]
        read_only_fields = ["id", "user", "created_at", "updated_at"]

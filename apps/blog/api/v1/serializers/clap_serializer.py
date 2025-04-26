from rest_framework import serializers

from apps.blog.models.post_model import Clap
from apps.blog.api.v1.serializers.post_serializer import PostSerializer


class GetClapSerializer(serializers.ModelSerializer):

    user = serializers.SerializerMethodField()
    post = PostSerializer(read_only=True)

    class Meta:
        model = Clap
        fields = ["id", "user", "post", "created_at", "updated_at"]

    def get_user(self, clap: Clap):
        return clap.user.email
    
    def get_post(self, clap: Clap):
        return clap.post.title


class PostClapSerializer(serializers.ModelSerializer):

    class Meta:
        model = Clap
        fields = ["post"]


class PutClapSerializer(serializers.ModelSerializer):

    class Meta:
        model = Clap
        fields = ["is_deleted"]

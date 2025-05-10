from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from apps.blog.api.v1.documents.post_document import PostDocument


class PostElasticSearchSerializer(DocumentSerializer):
    class Meta:
        document = PostDocument
        fields = [
            "id",
            "title",
            "slug",
            "body",
            "status",
            "created_at",
            "updated_at",
            "author_first_name",
            "author_last_name",
            "tags",
        ]

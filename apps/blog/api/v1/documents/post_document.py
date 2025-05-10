from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from apps.blog.models.post_model import Post


@registry.register_document
class PostDocument(Document):
    title = fields.TextField(
        fields={
            'raw': fields.KeywordField(),
            'suggest': fields.CompletionField(),
        }
    )
    body = fields.TextField(
        fields={
            'suggest': fields.CompletionField(),
        }
    )
    author_first_name = fields.TextField(
        attr="author.first_name",
        fields={
            'suggest': fields.CompletionField(),
        }
    )
    author_last_name = fields.TextField(
        attr="author.last_name",
        fields={
            'suggest': fields.CompletionField(),
        }
    )
    tags = fields.ListField(
        fields.TextField(
            fields={
                'suggest': fields.CompletionField(),
            }
        )
    )
    slug = fields.TextField()
    status = fields.TextField()
    created_at = fields.DateField()
    updated_at = fields.DateField()

    class Index:
        name = "post"
        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = Post
        fields = []

    def prepare_tags(self, instance):
        return [tag.name for tag in instance.tags.all()]

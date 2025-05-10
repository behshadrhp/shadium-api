from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from django_elasticsearch_dsl_drf.filter_backends import FilteringFilterBackend, SearchFilterBackend, OrderingFilterBackend, FunctionalSuggesterFilterBackend

from apps.blog.api.v1.documents.post_document import PostDocument
from apps.blog.api.v1.serializers.post_document_serializer import PostElasticSearchSerializer


class PostElasticSearchViewSet(DocumentViewSet):
    document = PostDocument
    serializer_class = PostElasticSearchSerializer
    lookup_field = "id"
    
    filter_backends = [
        SearchFilterBackend,
        OrderingFilterBackend,
        FunctionalSuggesterFilterBackend,
        FilteringFilterBackend,
    ]
    
    functional_suggester_fields = {
        "title": {
            "field": "title.suggest",
            "suggesters": ["edge_ngram", "phonetic"],
        },
        "body": {
            "field": "body.suggest",
            "suggesters": ["edge_ngram"],
        },
        "author_first_name": {
            "field": "author_first_name.suggest",
            "suggesters": ["edge_ngram"],
        },
        "author_last_name": {
            "field": "author_last_name.suggest",
            "suggesters": ["edge_ngram"],
        },
        "tags": {
            "field": "tags.suggest",
            "suggesters": ["edge_ngram"],
        }
    }
    
    search_fields = {
        "title": {"boost": 4},
        "body": {"boost": 2},
        "tags": None,
        "author_first_name": None,
        "author_last_name": None,
    }
    
    filter_fields = {
        "status": "status.raw",
        "author_first_name": "author_first_name.raw",
        "author_last_name": "author_last_name.raw",
    }
    
    ordering_fields = {
        "created_at": "created_at",
        "updated_at": "updated_at",
    }
    
    ordering = ["-created_at"]

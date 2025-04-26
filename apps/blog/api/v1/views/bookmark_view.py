from django.db import IntegrityError

from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from apps.blog.models.bookmark_model import BookMark
from apps.blog.api.v1.serializers.bookmark_serializer import GetBookMarkSerializer, PostBookMarkSerializer, PutBookMarkSerializer

from apps.blog.api.v1.exeptions.base_exception import AlreadyBookMarkedException


class BookMarkViewSet(ModelViewSet):

    http_method_names = ["get", "post", "put", "patch"]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ["post__title__icontains"]
    lookup_field = "id"

    def get_queryset(self):
        user = self.request.user
        return BookMark.objects.select_related("user", "post").all().filter(user=user, is_deleted=False)

    def get_serializer_class(self):
        if self.request.method == "GET":
            return GetBookMarkSerializer
        elif self.request.method == "POST":
            return PostBookMarkSerializer
        elif self.request.method == "PUT" or self.request.method == "PATCH":
            return PutBookMarkSerializer
    
    def perform_create(self, serializer):
        try:
            return serializer.save(user=self.request.user)
        except BookMark.DoesNotExist:
            raise ValidationError(
                {
                    "error": True,
                    "detail": "Invalid bookmark id provided.",
                    "code": 2005
                },
                code=400
            )
        except IntegrityError:
            raise AlreadyBookMarkedException
        
        except Exception as error:
            raise ValidationError(
                {
                    "error": True,
                    "detail": "Please try again later.",
                    "code": 2004,
                }
            )
    
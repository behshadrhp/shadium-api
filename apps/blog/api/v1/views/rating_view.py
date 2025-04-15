from django.db import IntegrityError

from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from apps.blog.models.rating_model import Rating
from apps.blog.api.v1.exeptions.rating_exception import AlreadyRatedException
from apps.blog.api.v1.serializers.rating_serializer import RatingSerializer


class RatingExploreViewSet(ModelViewSet):

    serializer_class = RatingSerializer
    http_method_names = ["get", "post", "put", "patch"]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset = ["rating_type"]
    search_fields = [
        "description__icontains", "post__title__icontains", 
    ]
    lookup_field = "id"

    def get_queryset(self):
        return Rating.objects.all()

    def perform_create(self, serializer):
        try:
            return serializer.save(user=self.request.user)
        except Rating.DoesNotExist:
            raise ValidationError(
                {
                    "error": True,
                    "detail": "Invalid post id provided.",
                    "code": 2003
                },
                code=400
            )
        except IntegrityError:
            raise AlreadyRatedException
        
        except Exception as error:
            raise ValidationError(
                {
                    "error": True,
                    "detail": "Please try again later.",
                    "code": 2002,
                }
            )
    
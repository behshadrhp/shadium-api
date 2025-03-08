from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from apps.account.models.profile_model import Profile
from apps.account.api.v1.serializers.profile_serializer import AllProfileSerializer
from apps.account.api.v1.serializers.profile_serializer import GetProfileSerializer, PutProfileSerializer

class ProfileViewSet(ModelViewSet):

    permission_classes = [IsAuthenticated]
    http_method_names = ["get", "put", "patch"]
    lookup_field = "id"

    def get_queryset(self):
        user = self.request.user
        queryset = Profile.objects.select_related("user").prefetch_related("following").filter(user=user)
        return queryset
    
    def get_serializer_class(self):
        if self.request.method == "GET":
            return GetProfileSerializer
        return PutProfileSerializer


class AllProfileViewSet(ModelViewSet):

    serializer_class = AllProfileSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ["get"]
    lookup_field = "id"

    def get_queryset(self):
        queryset = Profile.objects.select_related("user").prefetch_related("following").all()
        return queryset

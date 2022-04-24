from rest_framework import viewsets
from profiles_api import serializers, models


class UserProfileViewset(viewsets.ModelViewSet):
    """Create and update profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
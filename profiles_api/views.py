from rest_framework import viewsets, filters
from profiles_api import serializers, models, permisions
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


class UserProfileViewset(viewsets.ModelViewSet):
    """Create and update profiles"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permisions.UpdateOnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')


class UserLoginApiView(ObtainAuthToken):
    """Create authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
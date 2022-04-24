from rest_framework import viewsets, filters
from profiles_api import serializers, models, permisions
from rest_framework.authentication import TokenAuthentication


class UserProfileViewset(viewsets.ModelViewSet):
    """Create and update profiles"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permisions.UpdateOnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')

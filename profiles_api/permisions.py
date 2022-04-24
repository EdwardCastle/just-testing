from rest_framework import permissions


class UpdateOnProfile(permissions.BasePermission):
    """Allow users to edit they own profile"""

    def has_object_permission(self, request, view, obj):
        """Check if the user has permission"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


class UpdateOnStatus(permissions.BasePermission):
    """Allow update own status feed"""

    def has_object_permission(self, request, view, obj):
        """Check if the user has permission"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id

from rest_framework import permissions
from rest_framework.permissions import IsAdminUser

from contact.models import Contact


class ContactBelongsToUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        return obj.user.id == request.user.id


class IsSuperUser(IsAdminUser):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)
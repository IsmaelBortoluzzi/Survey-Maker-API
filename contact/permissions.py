from rest_framework import permissions

from contact.models import Contact


class ContactBelongsToUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        return obj.user.id == request.user.id
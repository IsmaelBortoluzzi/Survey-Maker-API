from rest_framework import permissions

from contact.models import Contact


class IsAuthor(permissions.BasePermission):
    def has_permission(self, request, view):
        contact = Contact.objects.filter(user__id=request.user.id).first()
        if contact is None or contact.is_author is False:
            return False
        return True
        
    def has_object_permission(self, request, view, obj):
        return super().has_object_permission(request, view, obj)


class IsOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        super().has_permission(request, view)

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user.id
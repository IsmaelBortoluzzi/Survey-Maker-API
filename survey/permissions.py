from rest_framework import permissions
from rest_framework_mongoengine.generics import get_object_or_404

from contact.models import Contact
from survey.mixins import IdParserMixin
from survey.models import Survey


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
        return super().has_permission(request, view)

    def has_object_permission(self, request, view, obj):
        print(obj.author, request.user.id)
        return obj.author == request.user.id


class IsOwnerOfParentSurvey(permissions.BasePermission):
    def has_permission(self, request, view):
        _id = IdParserMixin().parse_obj_id(_id=request.query_params.get('survey', None))
        survey = get_object_or_404(Survey.objects.all(), id=_id)
        if survey.author != request.user.id:
            return False
        return True

    def has_object_permission(self, request, view, obj):
        return True


class CanDeleteSurveyToRespond(permissions.BasePermission):
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        survey = get_object_or_404(Survey.objects.all(), id=obj.survey.pk)
        if survey.author != request.user.id:
            return False
        return True

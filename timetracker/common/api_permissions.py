from django.contrib.contenttypes.models import ContentType
from rest_framework.permissions import BasePermission

"""In this case we are going to have permissions on model level
 so I created some general permissions"""


class CanView(BasePermission):

    def has_permission(self, request, view):
        user = request.user
        obj = ContentType.objects.get_for_model(view.get_queryset().model)
        return user and user.has_perm(obj.app_label + '.view_' + obj.model)


class CanAdd(BasePermission):

    def has_permission(self, request, view):
        user = request.user
        obj = ContentType.objects.get_for_model(view.get_queryset().model)
        return user and user.has_perm(obj.app_label + '.add_' + obj.model)

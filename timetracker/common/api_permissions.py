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


class CanUpdate(BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        objs = ContentType.objects.get_for_model(view.get_queryset().model)
        client = obj.task.project.client
        client_users = client.client_users.all().values_list('user__id', flat=True)
        client_users = list(client_users)
        permission = user and user.has_perm(objs.app_label + '.change_' + objs.model) and user.id in client_users
        return permission

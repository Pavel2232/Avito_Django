
from rest_framework import permissions

class AdsPermission(permissions.BasePermission):


    def has_permission(self,request, view):

        if view.action == 'list':
            return True
        elif view.action == 'create':
            return request.user.is_authenticated
        elif view.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            return True


    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True

        if view.action in ['update', 'partial_update', 'destroy']:
            return obj.author == request.user or request.user.is_admin


class CommentPermission(permissions.BasePermission):


    def has_permission(self,request, view):

        if view.action == 'list':
            return True
        elif view.action == 'create':
            return request.user.is_authenticated
        elif view.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            return True


    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True

        if view.action in ['update', 'partial_update', 'destroy']:
            return obj.author == request.user
from rest_framework import permissions


class IsUser(permissions.BasePermission):
    def has_permission(self, request, view, obj):

        return obj.user == request.user
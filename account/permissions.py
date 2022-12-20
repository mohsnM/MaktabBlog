# Third-party imports.
from rest_framework.permissions import SAFE_METHODS, BasePermission


class HasAccess(BasePermission):
    def has_permission(self, request, view):
        return bool(request.method in SAFE_METHODS or request.user and request.user.is_staff)

    def has_object_permission(self, request, view, obj):
        return bool(request.method in SAFE_METHODS or request.user == obj or request.user.is_staff)

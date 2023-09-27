from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class IsEnrolled(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):
        if obj in request.user.profile.enrolled_products.all():
            return True

        return False

class IsProfileOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
    
    def has_object_permission(self, request, view, obj):
        if obj == request.user.profile:
            return True

        return False
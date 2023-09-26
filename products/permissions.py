from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class IsEnrolled(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):

        # доступ для администраторов
        if request.user.is_superuser:
            return True

        # если пользователь владелец продукта
        if request.user == obj.product_owner.user:
            return True

        # если записан на продукт 
        if obj in request.user.profile.enrolled_products.all():
            return True

        return False
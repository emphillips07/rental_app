from rest_framework.permissions import BasePermission

class IsStaff(BasePermission):
    def has_permission(self, request, view):
        level = request.user.level
        is_true = (level == "2")
        return bool(is_true and request.user.is_authenticated)
    
class IsManager(BasePermission):
    def has_permission(self, request, view):
        level = request.user.level
        is_true = (level == "1")
        return bool(is_true and request.user.is_authenticated)
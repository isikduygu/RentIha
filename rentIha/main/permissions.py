from rest_framework.permissions import BasePermission, SAFE_METHODS

# safe methodların içerisinde get ve head var kullanıcı delete post ve put yapamaz
class IsAdminUserOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True  # Sadece okuma izni ver
        return request.user and request.user.is_superuser
    

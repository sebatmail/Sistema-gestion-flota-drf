from rest_framework import permissions


class IsAdminOrReadOnlySelf(permissions.BasePermission):
    """
    Los administradores (is_staff) tienen acceso total.
    Los usuarios normales (choferes) solo pueden consultar (GET).
    """

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False

        # Permitir lectura (GET, HEAD, OPTIONS) a cualquier usuario autenticado
        if request.method in permissions.SAFE_METHODS:
            return True

        # Solo administradores pueden realizar mutaciones (POST, PUT, PATCH, DELETE)
        return request.user.is_staff

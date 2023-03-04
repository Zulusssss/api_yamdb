from rest_framework import permissions


class IsAdminOrSuperuserOrReadOnly(permissions.BasePermission):
    """
    Права админа, суперюзера, только чтение.
    """

    def has_permission(self, request, view):
        user = request.user
        return (request.method in permissions.SAFE_METHODS
                or (user.is_authenticated
                    and (user.is_admin
                         or user.is_superuser))
                )

    def has_object_permission(self, request, view, obj):
        user = request.user
        return (request.method in permissions.SAFE_METHODS
                or user.is_admin
                or user.is_superuser
                )


class IsAdminOrSuperuser(permissions.BasePermission):
    """
    Права админа, суперюзера.
    """

    def has_permission(self, request, view):
        user = request.user
        return (user.is_authenticated
                and (user.is_admin
                     or user.is_superuser)
                )

    def has_object_permission(self, request, view, obj):
        user = request.user
        return (user.is_admin
                or user.is_superuser
                )


class IsAdminModerAuthorOrReadonly(permissions.BasePermission):
    """
    Права админа, модератора, автора.
    """

    def has_permission(self, request, view):
        user = request.user
        return (request.method in permissions.SAFE_METHODS
                or user.is_authenticated
                )

    def has_object_permission(self, request, view, obj):
        user = request.user
        return (request.method in permissions.SAFE_METHODS
                or user.is_superuser
                or user.is_admin
                or user.is_moderator
                or user == obj.author
                )

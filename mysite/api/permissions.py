# api/permissions.py
from rest_framework import permissions


# https://www.django-rest-framework.org/api-guide/permissions/#custom-permissions
class IsStaffEditorPermission(permissions.DjangoModelPermissions):
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }
    # def has_permission(self, request, view):
    #     if not request.user.is_staff:
    #         return False
    #     return super().has_permission(request, view)

    # def has_permission(self, request, view):
    #     user = request.user
    #     print(user.get_all_permissions())
    #     if user.is_staff:
    #         if user.has_perm("myapp.view_book"):  # "app_name.verb_model_name"
    #             return True
    #         # if user.has_perm("myapp.change_book"):
    #         #     return True
    #         return False
    #     return False

    # def has_object_permission(self, request, view, obj):
    #     return obj.owner == request.user

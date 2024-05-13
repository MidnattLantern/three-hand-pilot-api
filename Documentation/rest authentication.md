REST framework allow you to switch authentication.
Inside the urls.py, add:
- `path('api-auth/', include('rest_framework.urls')),`

Permissions
---
Inside flynarc_api, create a permissions.py
Import: `from rest_framework import permissions`
Add the following content:
`
class IsOwnerOrReadOnly(permissions.BasePermission):
    """ Docstring """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
`
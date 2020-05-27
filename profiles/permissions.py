from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """ Allow users to edit their own profile. """

    def has_object_permission(self, request, view, obj):
        """ Check user is trying to update their own status. """

        if request.method in permissions.SAFE_METHODS:
            return True

        if hasattr(obj, 'userprofile'):
            return obj.userprofile.id == request.user.id
        else:
            return True

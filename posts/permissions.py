from rest_framework import permissions

"""Specifically we want to allow read-only for all requests but for any write
requests, such as edit or delete, the author must be the same as the current logged-
in user."""

class isAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Read-only permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the author of the post
        return obj.author == request.user


"""
We import permissions at the top and then create a custom class IsAuthorOrReadOnly
which extends BasePermission. 
https://github.com/encode/django-rest-framework/blob/master/rest_framework/permissions.py

Then we override has_object_permission. If a request
contains HTTP verbs included in SAFE_METHODS–a tuple containing GET, OPTIONS, and
HEAD–then it is a read-only request and permission is granted.

Otherwise the request is for a write of some kind, which means updating the API
resource so either create, delete, or edit functionality. In that case, we check if the
author of the object in question, which is our blog post obj.author matches the user
making the request request.user. 
"""
A Blog API using the full set of Django REST Framework features.

It will have users, permissions, and allow for full CRUD (Create-Read-Update-Delete)
functionality. Also exploring viewsets, routers, and documentation.

Create a directory for this project called blogapi. 
Then install Django in a new virtual environment create a new Django project (blog_project) and app for blog entries (posts).


We can view Post Detail page since read-only permissions are allowed. However we can not make any PUT or DELETE requests due to our custom IsAuthorOrReadOnly permission class.

Note that the generic views will only check the object-level permissions for views that retrieve a single model instance. If you require object-level filtering of list views–for a collection of instances–you’ll need to filter by overriding the initial queryset.


Best Practices:

Combine permissions with authentication for a more secure API.
When designing permissions, follow the principle of least privilege: users should only access what's necessary for their role.


Also Added Session and token authentication

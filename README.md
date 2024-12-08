# Blog API with Advanced Authentication and Authorization Using DRF

A **Blog API** built with Django and Django REST Framework (DRF), showcasing full CRUD functionality, user authentication, custom permissions, and a clean architecture. This project includes best practices and is designed to be beginner-friendly yet robust enough for production-level exploration.

---

## Features

- **CRUD Functionality**: Full Create-Read-Update-Delete operations for blog posts.
- **Custom Permissions**: `IsAuthorOrReadOnly` permission class to allow only authors to modify their posts while others have read-only access.
- **User Management**: User registration, login, and logout endpoints.
- **Authentication**: Session and token-based authentication for secure access.
- **Viewsets & Routers**: Simplified URL routing with DRF's `ViewSet` and `Router` capabilities.
- **Object-Level Permissions**: Ensures granular control over data access.
- **Best Practices**: Combines permissions with authentication to adhere to the principle of least privilege.

---
## Highlights

- **Custom Permissions**: IsAuthorOrReadOnly
```python
from rest_framework.permissions import BasePermission

class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user
```
- **ViewSets and Routers**:
```python
from rest_framework.routers import DefaultRouter
from posts.views import PostViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
]
```

## Best Practices
- **Authentication & Authorization**: DRF has built in basic and session authentication. Apart from that, I combined session and token authentication for flexibility. 
- **Principle of Least Privilege**: Users should only access resources necessary for their role.
- **Secure Endpoints**: I used DRF’s permissions module to restrict access.

Blog API
A fully-featured Blog API built with Django and Django REST Framework (DRF). This API supports user authentication, permissions, and CRUD functionality for blog posts. It is designed with best practices in mind, combining authentication and permissions for a secure and robust implementation.

Features
CRUD Functionality: Full Create, Read, Update, Delete operations for blog posts.
User Authentication: Supports session-based and token-based authentication.
Permissions: Implements a custom permission class (IsAuthorOrReadOnly) to allow:
Read-only access for all users.
Write, Update, and Delete permissions only for the author of the post.
Generic Views: Uses DRF's generic views for streamlined functionality.
Object-level Permissions: Ensures individual resource access control.
User Endpoints:
Registration
Login
Logout
Documentation: API endpoints are documented for ease of use.

Blog API Project
A Blog API built with Django and Django REST Framework (DRF), showcasing full CRUD functionality, user authentication, custom permissions, and a clean architecture. This project includes best practices and is designed to be beginner-friendly yet robust enough for production-level exploration.

Features
CRUD Functionality: Full Create-Read-Update-Delete operations for blog posts.
Custom Permissions: IsAuthorOrReadOnly permission class to allow only authors to modify their posts while others have read-only access.
User Management: User registration, login, and logout endpoints.
Authentication: Session and token-based authentication for secure access.
Viewsets & Routers: Simplified URL routing with DRF's ViewSet and Router capabilities.
Object-Level Permissions: Ensures granular control over data access.
Best Practices: Combines permissions with authentication to adhere to the principle of least privilege.

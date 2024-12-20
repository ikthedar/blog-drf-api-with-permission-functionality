from django.urls import path

from .views import PostList, PostDetail, UserList, UserDetail

urlpatterns = [
    path('users/', UserList.as_view()), # new
    path('users/<int:pk>/', UserDetail.as_view()),
    path('<int:pk>/', PostDetail.as_view()),
    path('', PostList.as_view()), # it will redirect from "api/v1/"
]
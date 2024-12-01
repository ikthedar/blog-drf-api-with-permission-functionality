from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer
from .permissions import isAuthorOrReadOnly


class PostList(generics.ListCreateAPIView):
#    permission_classes = (permissions.IsAuthenticated,) # removed this line since we added project-level permission
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (isAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer



# At the top of the file we import generics from Django REST Framework as well as
# our models and serializers files. Then we create two views. PostList uses the generic
# ListCreateAPIView while PostDetail uses the RetrieveUpdateDestroyAPIView.
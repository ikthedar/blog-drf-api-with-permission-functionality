from django.contrib.auth import get_user_model # new
from rest_framework import serializers

from .models import Post

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'author', 'title', 'body', 'created_at',)
        model = Post

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id', 'username',)


# At the top of the file we have imported Django REST Framework’s serializers class
# and our own models. Then we created a PostSerializer and added a Meta class where
# we specified which fields to include and explicitly set the model to use. 
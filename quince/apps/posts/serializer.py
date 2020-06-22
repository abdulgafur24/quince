from rest_framework import serializers
from account.serializer import UserSerializer
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'user', 'post_title', 'post_body', 'post_date')

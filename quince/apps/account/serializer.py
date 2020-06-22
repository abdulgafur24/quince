from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from .models import User


class UserCustomCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = (
            'id', 'email', 'username',
            'password', 'first_name',
            'last_name', 'biography',
            'is_active', 'is_private',
            'is_superuser'
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name',
                  'username', 'email', 'biography')

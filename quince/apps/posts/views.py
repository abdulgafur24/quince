from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Post, Comment


from rest_framework.views import APIView


from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .serializer import PostSerializer
from rest_framework import viewsets
from rest_framework.response import Response


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def index(request):
    posts = Post.objects.all()
    content = {'message': 'Hello, World!', 'data': posts}
    # content = {'message': 'Hello, World!'}
    return Response(content)


class PostViewSet(viewsets.ViewSet):
    # @api_view(['GET'])
    # @permission_classes([IsAuthenticated])
    def list(self, request):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

    # @api_view(['GET'])
    # @permission_classes([IsAuthenticated])
    def retrieve(self, request, pk=None):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

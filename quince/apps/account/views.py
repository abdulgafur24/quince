from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
# Create your views here.


@api_view(['GET'])
@permission_classes([IsAuthenticated])
# @permission_classes([])
def restricted(request):

    token = request.META.get('HTTP_AUTHORIZATION', '')
    print(token)
    return Response("Done", status=status.HTTP_200_OK)

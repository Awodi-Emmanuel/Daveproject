from django.shortcuts import render

# Create your views here.
from rest_framework import permissions
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response

from user.models import User
from user.serializers import UserSerializer


class UserView(UpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    @staticmethod
    def get(request):
        user = User.objects.get(id=request.GET.get('id'))
        user_serializer = UserSerializer(user)
        return Response(user_serializer.data, status=200)

    @staticmethod
    def put(request):
        user = User.objects.get(id=request.GET.get('id'))
        user_serializer = UserSerializer(user, data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=200)
        return Response(user_serializer.errors, status=500)

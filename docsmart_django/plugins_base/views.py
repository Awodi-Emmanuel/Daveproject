from django.shortcuts import render
from rest_framework import permissions, status
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.response import Response
from .serializers import AddPluginSerializer
from company.models import Company
from .backends import PluginAccessPermission
from roles.backends import OwnerPermission
from plugins_base.models import Plugin, AppTypes
from user.models import User


# Create your views here.


class AddPlugin(GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = AddPluginSerializer

    @staticmethod
    def post(request):
        serializer = AddPluginSerializer(data=request.data)
        if serializer.is_valid():
            company = Company.objects.get(id=request.data.get('company'))
            serializer.save(company=company)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddUserToPlugin(GenericAPIView):
    permission_classes = (permissions.IsAuthenticated, OwnerPermission, PluginAccessPermission)

    @staticmethod
    def post(request):

        if request.data.get('user') is not None and request.data.get('app') is not None:

            user = User.objects.get(id=request.data.get('user'))
            company = Company.objects.get(user__id=request.user.id)
            plugin = Plugin.objects.get(company=company, app=request.data.get('app'))

            if plugin:
                Plugin.grant_plugin_access(user, plugin)
                return Response({"message": "User granted access", "status": "success"}, status=status.HTTP_201_CREATED)

            return Response({"message": "Unable to grant access to user", "status": "failed"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({"message": "company or app cannot be missing", "status": "failed"},
                        status=status.HTTP_400_BAD_REQUEST)

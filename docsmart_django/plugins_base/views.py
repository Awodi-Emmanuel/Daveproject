from django.shortcuts import render
from rest_framework import permissions, status
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.response import Response
from .serializers import AddPluginSerializer
# Create your views here.
class CreateSalesOffer(GenericAPIView):

    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = AddPluginSerializer

    @staticmethod
    def post(request):
        serializer = AddPluginSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


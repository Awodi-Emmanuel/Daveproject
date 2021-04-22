from django.shortcuts import render
from .models import Company
from .serializers import CompanyUpdateSerializer
from rest_framework import status, permissions
from rest_framework.response import Response

# Create your views here.
class UpdateCompany(generics.UpdateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyUpdateSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.name = request.data.get("name")
        instance.save()

        serializer = self.get_serializer(instance)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)



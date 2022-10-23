from django.shortcuts import render

from roles.models import Role
from .models import Company
from .serializers import CompanyUpdateSerializer
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.generics import UpdateAPIView


# Create your views here.
class UpdateCompany(UpdateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyUpdateSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def update(self, request, *args, **kwargs):

        company = Company.objects.get(user__id=request.user.id).role()
        role = Role.objects.get(company=company.id)
        if role.role != 'OWNER':

            return Response({'message': 'User cannot update company data', 'status': 'failed'}, status.HTTP_200_OK)

        instance = self.get_object()
        instance.name = request.data.get("name")
        instance.save()

        serializer = self.get_serializer(instance)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data, status.HTTP_200_OK)

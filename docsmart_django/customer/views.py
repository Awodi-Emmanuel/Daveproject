from django.shortcuts import render
from rest_framework import permissions, status
from .serializer import CreateCustomerSerializer
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from company.models import Company
import json
from django.forms.models import model_to_dict
from customer import serializer

# Create your views here.

class CreateCustomer(GenericAPIView):

    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = CreateCustomerSerializer

    @staticmethod
    def post(request):
        if not request.data.get('customers'):

            customer_serializer = CreateCustomerSerializer(data=request.data)
            if customer_serializer.is_valid():

                related_company = Company.objects.get(user__id=request.user.id)
                customer_serializer.save(related_company=related_company)
                return Response(customer_serializer.data, status=status.HTTP_201_CREATED)
            
            return Response(customer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        errors = []
        customers = []

        for c in request.data.get('customers'):

            customer_serializer = CreateCustomerSerializer(data=c)
            if customer_serializer.is_valid():

                related_company = Company.objects.get(user__id=request.user.id)
                customer_serializer.save(related_company=related_company)
                customers.append(customer_serializer.data)
            else:
                errors.append(customer_serializer.errors)

        if errors:

            return Response(errors, status=status.HTTP_400_BAD_REQUEST)    

        return Response(customers, status=status.HTTP_201_CREATED)
            

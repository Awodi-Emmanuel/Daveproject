from django.shortcuts import render

# Create your views here.
from rest_framework import permissions, status
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.response import Response

from documents.serializers import DocumentSerializer
from sales.serializers import CreatePaymentSchedule, CreateSalesOfferSerializer, RetrieveSalesOfferSerializer
from sales.models import Sales


class CreateSalesOffer(GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = CreateSalesOfferSerializer, CreatePaymentSchedule

    @staticmethod
    def post(request):

        sale_serializer = CreateSalesOfferSerializer(data=request.data)
        payment_serializer = CreatePaymentSchedule(data=request.data)

        print(payment_serializer.is_valid())

        if payment_serializer.is_valid() == False and sale_serializer.is_valid():
            
            sale_serializer.save(owner=request.user)
            response_data = {'sale_object': sale_serializer.data}
            return Response(response_data, status=status.HTTP_201_CREATED)

        if sale_serializer.is_valid() and payment_serializer.is_valid():
            
            schedule = payment_serializer.save()
            sale_serializer.save(payment_schedule = schedule, owner=request.user)

            response_data = {'sale_object': sale_serializer.data, 'schedule_object': payment_serializer.data}
            return Response(response_data, status=status.HTTP_201_CREATED)

        # if request.data.get('customer'):

        #     for c in request.data.get('customer'):



            

        else:

            sale_serializer.is_valid()
            payment_serializer.is_valid()
            error_data = {'sale_error': sale_serializer.errors, 'schedule_error': payment_serializer.errors}
            return Response(error_data, status=status.HTTP_400_BAD_REQUEST)


class RetrieveSalesOffer(ListCreateAPIView):
    serializer_class = RetrieveSalesOfferSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Sales.objects.filter(owner=self.request.user)

from django.shortcuts import render

# Create your views here.
from rest_framework import permissions, status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from documents.serializers import DocumentSerializer

# class CreateDocument(GenericAPIView):
#     serializer_class = DocumentSerializer
#     permission_classes = (permissions.IsAuthenticated,)
#
#     @staticmethod
#     def post(request):
#         document_serializer = DocumentSerializer(data=request.data)
#
#         if document_serializer.is_valid():
#             document_serializer.save()
#             return Response({'message': 'Document created successfully'}, status=status.HTTP_201_CREATED)
#
#         return Response(document_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
from sales.serializers import CreateSalesOfferSerializer, CreatePaymentSchedule


class CreateSalesOffer(GenericAPIView):
    serializer_class = CreateSalesOfferSerializer, CreatePaymentSchedule

    @staticmethod
    def post(request):

        sale_serializer = CreateSalesOfferSerializer(data=request.data)
        payment_serializer = CreatePaymentSchedule(data=request.data)

        if sale_serializer.is_valid() and payment_serializer.is_valid():

            schedule = payment_serializer.save()

            sale = sale_serializer.save(payment_schedule=schedule.id)

            response_data = {'sale_object': sale.data, 'schedule_object': schedule.data}
            return Response(response_data, status=status.HTTP_201_CREATED)

        else:

            sale_serializer.is_valid()
            payment_serializer.is_valid()
            error_data = {'sale_error': sale_serializer.errors, 'schedule_error': payment_serializer.errors}
            return Response(error_data, status=status.HTTP_400_BAD_REQUEST)

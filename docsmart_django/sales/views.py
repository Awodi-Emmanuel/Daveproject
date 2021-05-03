# Create your views here.
from rest_framework import permissions, status
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.response import Response
from customer.serializer import CreateCustomerSerializer
from logs.models import Logs
from sales.serializers import CreatePaymentSchedule, CreateSalesOfferSerializer, RetrieveSalesOfferSerializer
from sales.models import Sales
from company.models import Company


class CreateSalesOffer(GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = CreateSalesOfferSerializer, CreatePaymentSchedule, CreateCustomerSerializer

    @staticmethod
    def post(request):

        sale_serializer = CreateSalesOfferSerializer(data=request.data)
        payment_serializer = CreatePaymentSchedule(data=request.data)

        if not payment_serializer.is_valid() and sale_serializer.is_valid():

            company = Company.objects.get(user__id=request.user.id)
            offer = sale_serializer.save(owner=request.user, related_company=company)

            if request.data.get('customers'):

                for c in request.data.get('customers'):
                    Sales.add_customer_to_offer(customer=c, offer=offer)

            if request.data.get('lines'):

                for line in request.data.get('lines'):
                    Sales.add_line_to_offer(line=line, offer=offer)

            Logs.objects.create_log(performed_by=request.user.id, affected_user=request.user.id,
                                    loggable=offer, action='Create Sales Offer')
            response_data = {'sale_object': sale_serializer.data}
            return Response(response_data, status=status.HTTP_201_CREATED)

        if sale_serializer.is_valid() and payment_serializer.is_valid():

            schedule = payment_serializer.save()
            company = Company.objects.get(user__id=request.user.id)
            offer = sale_serializer.save(payment_schedule=schedule, owner=request.user, related_company=company)

            if request.data.get('customers'):

                for c in request.data.get('customers'):
                    Sales.add_customer_to_offer(customer=c, offer=offer)

            if request.data.get('lines'):

                for line in request.data.get('lines'):
                    Sales.add_line_to_offer(line=line, offer=offer)

            Logs.objects.create_log(performed_by=request.user.id, affected_user=request.user.id,
                                    loggable=offer, action='Create Sales Offer')
            response_data = {'sale_object': sale_serializer.data, 'schedule_object': payment_serializer.data}
            return Response(response_data, status=status.HTTP_201_CREATED)
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

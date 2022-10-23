# Create your views here.
from rest_framework import permissions, status, serializers
from rest_framework.generics import GenericAPIView, ListCreateAPIView, UpdateAPIView
from rest_framework.response import Response
from customer.serializer import CreateCustomerSerializer
from logs.models import Logs
from plugins_base.backends import CompanyPluginAccessPermission, UserPluginAccessPermission
from sales.backends import OwnsSalesOffer
from sales.helpers import Send
from sales.serializers import CreatePaymentSchedule, RetrieveSalesOfferSerializer, \
    OfferSerializer
from sales.models import Sales
from company.models import Company
from django.contrib.contenttypes.models import ContentType


class CreateSalesOffer(GenericAPIView):
    permission_classes = (permissions.IsAuthenticated, CompanyPluginAccessPermission, UserPluginAccessPermission)
    serializer_class = OfferSerializer, CreatePaymentSchedule, CreateCustomerSerializer

    @staticmethod
    def post(request):

        sale_serializer = OfferSerializer(data=request.data)
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

            Logs.objects.create_log(performed_by=request.user, affected_user=request.user,
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

            Logs.objects.create_log(performed_by=request.user, affected_user=request.user, object_id=offer.id,
                                    loggable=ContentType.objects.get_for_model(offer), action='Create Sales Offer')
            response_data = {'sale_object': sale_serializer.data, 'schedule_object': payment_serializer.data}
            return Response(response_data, status=status.HTTP_201_CREATED)

        else:

            sale_serializer.is_valid()
            payment_serializer.is_valid()
            error_data = {'sale_error': sale_serializer.errors, 'schedule_error': payment_serializer.errors}
            return Response(error_data, status=status.HTTP_400_BAD_REQUEST)


class UpdateSalesOffer(UpdateAPIView):
    serializer_class = OfferSerializer
    permission_classes = (permissions.IsAuthenticated, CompanyPluginAccessPermission,
                          UserPluginAccessPermission, OwnsSalesOffer)

    @staticmethod
    def put(request):
        offer = Sales.objects.get(id=request.GET.get('offer'), owner=request.user)
        offer_serializer = OfferSerializer(offer, data=request.data)
        if offer_serializer.is_valid():
            offer_serializer.save()
            return Response(offer_serializer.data, status=200)
        return Response(offer_serializer.errors, status=500)


class AddCustomersToOffer(ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated, CompanyPluginAccessPermission,
                          UserPluginAccessPermission, OwnsSalesOffer)

    def post(self, request, *args, **kwargs):
        offer = Sales.objects.get(id=self.request.GET.get('offer'))
        if request.data.get('customers'):
            for c in request.data.get('customers'):
                Sales.add_customer_to_offer(customer=c, offer=offer)
            return Response({'message': 'Customers added successfully', 'status': 'success'}, 200)
        return Response({'message': 'Customers added successfully', 'status': 'success'}, 200)


class AddLinesToOffer(ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated, CompanyPluginAccessPermission,
                          UserPluginAccessPermission, OwnsSalesOffer)

    def post(self, request, *args, **kwargs):
        offer = Sales.objects.get(id=self.request.GET.get('offer'))
        if request.data.get('lines'):
            for l in request.data.get('lines'):
                Sales.add_line_to_offer(line=l, offer=offer)
            return Response({'message': 'Lines added successfully', 'status': 'success'}, 200)
        return Response({'message': 'Lines added successfully', 'status': 'success'}, 200)


class RetrieveSingleSalesOffer(ListCreateAPIView):
    serializer_class = RetrieveSalesOfferSerializer
    permission_classes = (permissions.IsAuthenticated, CompanyPluginAccessPermission, UserPluginAccessPermission)

    def get(self, request, *args, **kwargs):
        offer_serializer = RetrieveSalesOfferSerializer(Sales.objects.get(id=self.request.GET.get('offer')))
        return Response(offer_serializer.data)


class RetrieveSalesOffer(ListCreateAPIView):
    serializer_class = RetrieveSalesOfferSerializer
    permission_classes = (permissions.IsAuthenticated, CompanyPluginAccessPermission, UserPluginAccessPermission)

    def get_queryset(self):
        return Sales.objects.filter(owner=self.request.user)


class SendSalesOffer(GenericAPIView):
    permission_classes = (permissions.IsAuthenticated, CompanyPluginAccessPermission,
                          UserPluginAccessPermission, OwnsSalesOffer)

    def get(self, request, *args, **kwargs):
        try:
            offer = Sales.objects.get(id=self.request.GET.get('offer'))
            Send.offer(offer)
            return Response({'message': 'Offer sent successfully', 'status': 'success'}, 200)
        except Exception:
            return Response({'message': 'Unable to send offer', 'status': 'failed'}, 200)


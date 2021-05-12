from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from customer.models import Customer
from bankid.helpers import BankIdHandler
from bankid.models import SignedDocuments
from sales.models import Sales


class SignDocument(GenericAPIView):

    @staticmethod
    def get(request):
        if request.GET.get('offer') and request.GET.get('customer'):

            try:

                offer = Sales.objects.get(id=request.GET.get('offer'))
                ip = request.META.get("REMOTE_ADDR")
                customer = Customer.objects.get(id=request.GET.get('customer'))
                if offer.customer.get(id=customer.id):
                    result = BankIdHandler.sign_document(offer, ip, customer)
                    print(result)
                    return Response(result, status=200)

            except Exception:

                return Response({'message': 'Unable to sign document', 'status': 'failed'}, status=500)

        return Response({'message': 'document cannot be missing', 'status': 'failed'}, status=500)


class CollectStatus(GenericAPIView):

    @staticmethod
    def post(request):
        if request.data.get('signid'):

            try:
                signed_document = SignedDocuments.objects.get(id=request.data.get('signid'))
                result = BankIdHandler.collect_status(signed_document.data.orderRef)
                print(result)
                return Response(result, status=200)

            except Exception:
                return Response({'message': 'Unable to get document status', 'status': 'failed'}, status=500)

        return Response({'message': 'signid cannot be missing', 'status': 'fail0ed'}, status=500)

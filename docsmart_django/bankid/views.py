from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from bankid.helpers import BankIdHandler
from bankid.models import SignedDocuments
from documents.models import Document


# Create your views here.

class SignDocument(GenericAPIView):

    @staticmethod
    def post(request):
        if request.data.get('document'):

            try:
                document = Document.objects.get(id=request.data.get('document'))
                ip = request.META.get("REMOTE_ADDR")
                result = BankIdHandler.sign_document(document, ip)
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

        return Response({'message': 'signid cannot be missing', 'status': 'failed'}, status=500)

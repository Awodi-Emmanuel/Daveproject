from rest_framework.generics import GenericAPIView
from .serializers import DocumentSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class CreateDocument(GenericAPIView):
    serializer_class = DocumentSerializer

    def post(self, request):

        document_serializer = DocumentSerializer(data=request.data)

        if document_serializer.is_valid():
            
            document_serializer.save()
            return Response(document_serializer.data, status=status.HTTP_201_CREATED)

        return Response(document_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from rest_framework.generics import GenericAPIView
from .serializers import DocumentSerializer, FetchSerializer
from rest_framework.response import Response
from rest_framework import status


class CreateDocument(GenericAPIView):
    serializer_class = DocumentSerializer

    @staticmethod
    def post(request):
        document_serializer = DocumentSerializer(data=request.data)

        if document_serializer.is_valid():
            document_serializer.save()
            return Response({'message': 'Document created successfully'}, status=status.HTTP_201_CREATED)

        return Response(document_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FetchAccessibleDocuments(GenericAPIView):
    serializer_class = FetchSerializer

    @staticmethod
    def post(request):
        serializer = FetchSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Document created successfully'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from rest_framework.generics import GenericAPIView, ListCreateAPIView
from .serializers import DocumentSerializer, FetchSerializer
from permissions.models import DocumentPermission
from rest_framework.response import Response
from rest_framework import status, permissions, serializers
from .classes.folders import path_to_dict


class CreateDocument(GenericAPIView):
    serializer_class = DocumentSerializer

    @staticmethod
    def post(request):
        document_serializer = DocumentSerializer(data=request.data)

        if document_serializer.is_valid():
            document_serializer.save()
            return Response({'message': 'Document created successfully'}, status=status.HTTP_201_CREATED)

        return Response(document_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FetchDocument(ListCreateAPIView):
    serializer_class = FetchSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return DocumentPermission.objects.filter(user_id=self.request.user)


class FetchUserFolders(GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    @staticmethod
    def get(request):

        try:

            structure = path_to_dict('/var/www/html/connectivo/docsmart/docsmart_django/documents/migrations')
            return Response(structure, status=status.HTTP_200_OK)

        except Exception:

            return Response({"message": "We're unabke to fecth the users folder structure"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

from rest_framework.generics import GenericAPIView, ListCreateAPIView
from .serializers import DocumentSerializer, FetchSerializer
from permissions.models import DocumentPermission
from rest_framework.response import Response
from rest_framework import status, permissions
from .classes.generator import Generator


class CreateDocument(GenericAPIView):
    serializer_class = DocumentSerializer

    @staticmethod
    def post(request):
        document_serializer = DocumentSerializer(data=request.data)

        if document_serializer.is_valid():
            document_serializer.save()
            return Response({'message': 'Document created successfully'}, status=status.HTTP_201_CREATED)

        return Response(document_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FetchUserDocument(ListCreateAPIView):
    serializer_class = FetchSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return DocumentPermission.objects.filter(user_id=self.request.user)


class FetchUserFolderStructureWithPermissions(GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    @staticmethod
    def get(request):
        
        try:

            structure = Generator.generate_user_folder_object(str(request.user.id))

            return Response(structure, status=status.HTTP_200_OK)

        except Exception:

            return Response({"message": "We're unable to fetch the users folder structure"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

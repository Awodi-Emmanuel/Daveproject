from rest_framework.generics import GenericAPIView, ListCreateAPIView

from .models import Document
from .serializers import DocumentSerializer, FetchSerializer, FetchUserDocumentsSerializer
from permissions.models import DocumentPermission
from rest_framework.response import Response
from rest_framework import status, permissions
from .classes.generator import Generator
from .classes.directory import Directory
from .classes.files import Files


class CreateDocument(GenericAPIView):
    serializer_class = DocumentSerializer
    permission_classes = (permissions.IsAuthenticated,)

    @staticmethod
    def post(request):
        document_serializer = DocumentSerializer(data=request.data)

        if document_serializer.is_valid():
            document_serializer.save()
            return Response({'message': 'Document created successfully'}, status=status.HTTP_201_CREATED)

        return Response(document_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteSingleUserDocument(GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    @staticmethod
    def post(request):

        document_id = request.data.get("document_id")
        print(document_id)

        if document_id is None:
            return Response({'message': 'document_id cannot be null', 'status': 'failed'},
                            status=status.HTTP_400_BAD_REQUEST)
        
        # try:

        file = Files.delete_single_user_document(document_id, str(request.user.id))
        return Response(file, status=status.HTTP_200_OK)

        # except Exception:
        
        #     return Response({"message": "We're unable to delete this document"},
        #                     status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class FetchUserDocument(ListCreateAPIView):
    serializer_class = FetchUserDocumentsSerializer
    # serializer_class = FetchSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        
        return Document.objects.filter(company_id__isnull=True, permissions__user_id=self.request.user)


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


class FetchCompanyFolderStructureWithPermissions(GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    @staticmethod
    def get(request):
        
        try:

            structure = Generator.generate_company_folder_object(str(request.user.id))
            return Response(structure, status=status.HTTP_200_OK)

        except Exception:
        
            return Response({"message": "We're unable to fetch the users folder structure"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CreateSingleUserDirectory(GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    @staticmethod
    def post(request):

        try:

            directory_name = request.data.get("folder_name")
            current_directory_path = request.data.get("current_path")

            if directory_name is None or current_directory_path is None:
                return Response({'message': 'folder_name or folder_path is missing', 'status': 'failed'},
                                status=status.HTTP_400_BAD_REQUEST)

            new_directory = Directory.create_single_directory(str(request.user.id),
                                                              current_directory_path, directory_name)

            return Response(new_directory, status=status.HTTP_200_OK)

        except Exception:

            return Response({"message": "We're unable to create the folder"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

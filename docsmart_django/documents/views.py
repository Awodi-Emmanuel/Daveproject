from rest_framework.generics import GenericAPIView, ListCreateAPIView

from .models import Document
from .serializers import DocumentSerializer, FetchUserDocumentsSerializer
from rest_framework.response import Response
from rest_framework import status, permissions
from .classes.generator import Generator
from .classes.directory import Directory
from .classes.files import Files
from .classes.access import Access


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

        try:

            file = Files.delete_single_user_document(document_id, str(request.user.id))
            return Response(file, status=status.HTTP_200_OK)

        except Exception:

            return Response({"message": "We're unable to delete this document"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DeleteSingleCompanyDocument(GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    @staticmethod
    def post(request):

        document_id = request.data.get("document_id")
        print(document_id)

        if document_id is None:
            return Response({'message': 'document_id cannot be null', 'status': 'failed'},
                            status=status.HTTP_400_BAD_REQUEST)

        try:

            file = Files.delete_single_company_document(document_id, str(request.user.id))
            return Response(file, status=status.HTTP_200_OK)

        except Exception:

            return Response({"message": "We're unable to delete this document"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class FetchUserDocument(ListCreateAPIView):
    serializer_class = FetchUserDocumentsSerializer
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

            if directory_name is None:
                return Response({'message': 'folder_name', 'status': 'failed'},
                                status=status.HTTP_400_BAD_REQUEST)

            new_directory = Directory.create_single_directory(str(request.user.id),
                                                              current_directory_path, directory_name)

            return Response(new_directory, status=status.HTTP_200_OK)

        except Exception:

            return Response({"message": "We're unable to create the folder"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GrantAccess(GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    @staticmethod
    def post(request):

        receiving_user = request.data.get("receiving_user")
        document_id = request.data.get("document_id")
        permissions = request.data.get("permissions")

        if receiving_user is None or document_id is None or permissions is None:
                return Response({'message': 'receiving_user, document_id or permissions cannot be empty', 'status': 'failed'},
                                status=status.HTTP_400_BAD_REQUEST)
        try:

            granting_user = request.user
            access = Access.grant_access(recieving_user= receiving_user, granting_user= granting_user, document_id= document_id,
            read= permissions.read, write= permissions.write, delete= permissions.delete )

            return Response(access, status=status.HTTP_200_OK if access.get('status') == "success" else status.HTTP_500_INTERNAL_SERVER_ERROR)

        except Exception:

            return Response({"message": "We're unable to grant access to specified user"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class RevokeAccess(GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    @staticmethod
    def post(request):

        revoked_user = request.data.get("revoked_user")
        document_id = request.data.get("document_id")
        # permissions = request.data.get("permissions")
        #  or permissions is None

        if revoked_user is None or document_id is None:
                return Response({'message': 'revoked_user, document_id or permissions cannot be empty', 'status': 'failed'},
                                status=status.HTTP_400_BAD_REQUEST)
        try:

            revoking_user = request.user
            access = Access.revoke_access(revoking_user= revoked_user, revoked_user= revoked_user, document_id=document_id)


            return Response(access, status=status.HTTP_200_OK if access.get('status') == "success" else status.HTTP_500_INTERNAL_SERVER_ERROR)

        except Exception:

            return Response({"message": "We're unable to grant access to specified user"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)git 
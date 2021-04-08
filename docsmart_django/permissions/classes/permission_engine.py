from documents.models import Document
from permissions.models import DocumentPermission


class Engine:

    @staticmethod
    def fetch_accessible_files(user):
        return Document.objects.filter(company_id__isnull=True, user_id=user)

    @staticmethod
    def fetch_accessible_files_by_name(file_name, user):
        return Document.objects.filter(company_id__isnull=True, name=file_name, permissions__user_id=user)
        # return DocumentPermission.objects.filter(document_id__name=file_name)

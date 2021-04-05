from permissions.models import DocumentPermission


class Engine:

    @staticmethod
    def fetch_accessible_files(user):
        
        return DocumentPermission.objects.filter(user_id=user)

    @staticmethod
    def fetch_accessible_files_by_name(file_name):
        return DocumentPermission.objects.filter(document_id__name=file_name)

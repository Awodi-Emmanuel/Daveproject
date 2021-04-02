from permissions.models import DocumentPermission


class Engine:

    @staticmethod
    def fetch_accessible_files(user):
        
        return DocumentPermission.objects.filter(user_id=user)

        

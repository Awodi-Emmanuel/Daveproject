from permissions.models import DocumentPermission


class Engine:

    @staticmethod
    def fetch_accessible_files(user):
        permission_manager = DocumentPermission.objects.filter(user_id=user)

        for permissions in permission_manager:

            print(permissions.path)

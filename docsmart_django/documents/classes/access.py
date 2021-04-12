from documents.models import Document
from django.contrib.auth import get_user_model
from permissions.models import DocumentPermission

class Access:

    @staticmethod
    def grant_access(recieving_user, granting_user, document_id, read, write, delete):

        permission = DocumentPermission.objects.get(user_id=granting_user, document_id= document_id)
        if(permission.can_view):

            document = Document.objects.get(id=document_id)
            user = get_user_model().objects.get(id=recieving_user)
            new_permission = DocumentPermission.objects.grant_basic_permissions(document_id=document, user_id=user,
            can_view=read, can_edit=write, can_delete=delete)
            Document.objects.grant_access(new_permission, user)

            return {"message": "Access granted", "status": "success"}

        else:

            return {"message": "User does not have permissions to grant access", "status": "failed"}



    @staticmethod
    def revoke_access(revoking_user, revoked_user, document_id):

        permission = DocumentPermission.objects.get(user_id=revoking_user, document_id= document_id)

        if(permission.can_view):

          user = get_user_model().objects.get(id=revoked_user)
          document_permission = DocumentPermission.objects.get(user_id=revoked_user, document_id= revoked_user)
          Document.objects.revoke_access(document_permission, user)
          document_permission.delete()

          return {"message": "Access revoked", "status": "success"}

        else:

            return {"message": "User does not have permissions to revoke access", "status": "failed"}
          



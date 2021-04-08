from ..models import Document
from permissions.models import DocumentPermission

class Files:

    @staticmethod
    def delete_single_user_document(document_id, user_id):
        
        permission = DocumentPermission.objects.get(user_id=user_id, document_id=document_id)

        if permission and permission.can_delete:
            
            Document.objects.revoke_access(permission.id, document_id)
            #.objects.get(id=document_id).delete()
            
        

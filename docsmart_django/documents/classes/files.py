from ..models import Document
from permissions.models import DocumentPermission
from company.models import Company

class Files:

    @staticmethod
    def delete_single_user_document(document_id, user_id):

        try:
        
            permission = DocumentPermission.objects.get(user_id=user_id, document_id=document_id)
            document = Document.objects.get(id=document_id)

            if not document:

                return {"message": "Missing or invaid document", "status": "failed"} 

            if permission and permission.can_delete:
                
                document.permissions.remove(permission)
                permission.delete()
                document.delete()

                return {"message": "Document deleted successfully", "status": "success"}

            return {"message": "User does not have delete permission", "status": "failed"}

        except Exception:
            
             return {"message": "User does not have delete permission or document does not exist", "status": "failed"}   



    @staticmethod
    def delete_single_company_document(document_id, user_id):

        try:
        
            company = Company.objects.get(user__id=user_id)
            document = Document.objects.get(id=document_id)

            # print(company.id)
            # print(document.company_id.id)

            if company.id != document.company_id.id:

                return {"message": "User does not have delete permission for this document", "status": "failed"} 


            if not document:

                return {"message": "Missing or invaid document", "status": "failed"} 


            permission = DocumentPermission.objects.get(user_id=user_id, document_id=document_id)

            if permission and permission.can_delete:
                
                document.permissions.remove(permission)
                permission.delete()
                document.delete()

                return {"message": "Document deleted successfully", "status": "success"}

            return {"message": "User does not have delete permission", "status": "failed"}

        except Exception:
            
             return {"message": "User does not have delete permission or document does not exist", "status": "failed"}   
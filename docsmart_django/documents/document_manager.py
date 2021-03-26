from django.db import models
from django.contrib.auth import get_user_model



class DocumentsManager(models.Manager):
    """ 
    custom documents model
    """
    def create_document(
            self,
            name,
            path,
            company_id,
            created_by,
            last_edited_by,
            
        ):
        """Create basic document."""
        if not name:
            raise ValueError('Document must have a name')
        if not path:
            raise ValueError('Document must have a path')
        if not company_id:
            raise ValueError('Document must have a company')
        if not created_by:
            raise ValueError('Document must have a user that created it')
        if not last_edited_by:
            raise ValueError('Document must have a user who last edited it')

        document = self.model(
            name=name.lower(),
            path = path,
            company_id = company_id,
            created_by = created_by,
            last_edited_by = last_edited_by,  
        )

        document.save(using=self._db)
        permission = PermissionsManager.grant_basic_permissions(self=self, document_id= document.id, user_id= created_by)
        self.grant_access(permissions=permission, document=document)
        return document


class PermissionsManager(models.Manager):
    """ 
    custom permission model
    """
    def grant_basic_permissions(
            self,
            document_id,
            user_id,
            can_view=True,
            can_edit=False,
            can_delete=False,
            
        ):

        """Grant basic permission document."""
        if not document_id:
            raise ValueError('Document must have a name')
        if not user_id:
            raise ValueError('Document must have a path')


        permissions = self.model(
            document_id=document_id,
            user_id = user_id,
            can_view = can_view,
            can_edit = can_edit,
            can_delete = can_delete,  
        )

        permissions.save(using=self._db)
        return permissions
from django.db import models


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
            user_id=user_id,
            can_view=can_view,
            can_edit=can_edit,
            can_delete=can_delete,
        )

        permissions.save(using=self._db)
        return permissions

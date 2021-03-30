from django.db import models
from company.models import Company
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

        company = None

        try:

            company = Company.objects.get(id=company_id)

        except Exception:

            raise ValueError('Company does not exist')

        creating_user = get_user_model().objects.get(id=created_by)
        editing_user = get_user_model().objects.get(id=last_edited_by)

        document = self.model(
            name=name.lower(),
            path=path,
            company_id=company,
            created_by=creating_user,
            last_edited_by=editing_user,
        )

        document.save(using=self._db)
        return document

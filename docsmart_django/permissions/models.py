from django.db import models

from company.models import Company
from .manager import PermissionsManager
from user.models import User


class DocumentPermission(models.Model):
    document_id = models.ForeignKey('documents.Document', on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="permission_owner")
    can_view = models.BooleanField(verbose_name="Can View", name="can_view", default=True)
    can_edit = models.BooleanField(verbose_name="Can Edit", default=False)
    can_delete = models.BooleanField(verbose_name="Can Delete", default=False)

    REQUIRED_FIELDS = ['document_id', 'user_id', 'can_view', 'can_edit', 'can_delete', ]

    objects = PermissionsManager()

    class Meta:
        verbose_name = "DocumentPermission"
        verbose_name_plural = "DocumentPermissions"

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse("DocumentPermission_detail", kwargs={"pk": self.pk})

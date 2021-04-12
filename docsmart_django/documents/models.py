from django.db import models
from user.models import User
from company.models import Company
from documents.manager import DocumentsManager
from permissions.models import DocumentPermission


# Create your models here.

class Document(models.Model):
    """Document model."""
    name = models.CharField(max_length=255, null=False)
    path = models.CharField(max_length=255, null=False)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, )
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="creator")
    permissions = models.ManyToManyField(DocumentPermission, verbose_name="Permission", blank=True)
    date_last_edited = models.DateTimeField(auto_now_add=True)
    last_edited_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    REQUIRED_FIELDS = ['name', 'created_by', 'path', 'last_edited_by', ]

    objects = DocumentsManager()

    @classmethod
    def grant_access(cls, permissions, document):
        document.permissions.add(permissions)

    @classmethod
    def revoke_access(cls, permissions, document):
        document.permissions.remove(permissions)

    class Meta:
        verbose_name = "Document"
        verbose_name_plural = "Documents"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Document_detail", kwargs={"pk": self.pk})

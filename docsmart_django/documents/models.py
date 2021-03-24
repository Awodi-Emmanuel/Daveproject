from django.db import models
from user.models import User
from company.models import Company
from documents.document_manager import DocumentsManager

# Create your models here.

class Document(models.Model):

    """Document model."""
    name = models.CharField(max_length=255, null=False)
    path = models.CharField(max_length=255, null= False)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE, null=True,)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="creator")
    permissions = models.ManyToManyField("document.DocumentPermission", verbose_name="Permission",blank=True)
    date_last_edited = models.DateTimeField(auto_now_add=True)
    last_edited_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    

    REQUIRED_FIELDS = ['name', 'created_by', 'path', 'company_id', 'last_edited_by',]

    objects = DocumentsManager()


    @classmethod
    def grant_ccess(cls, permissions, document):
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



    class DocumentPermission(models.Model):
        
          
        document_id = models.ForeignKey(Document, on_delete=models.CASCADE)
        user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="permission_owner")
        can_view = models.BooleanField(verbose_name="Can View", name="can_view",default=True)
        can_edit = models.BooleanField(verbose_name="Can Edit", default=False)
        can_delete = models.BooleanField(verbose_name="Can Delete", default=False)


        REQUIRED_FIELDS = ['document_id', 'user_id', 'can_view', 'can_edit', 'can_delete',]

        objects = DocumentsManager()
    
        class Meta:
            verbose_name = "DocumentPermission"
            verbose_name_plural = "DocumentPermissions"
    
        def __str__(self):
            return self.name
    
        def get_absolute_url(self):
            return reverse("DocumentPermission_detail", kwargs={"pk": self.pk})
    


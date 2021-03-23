from django.db import models

# Create your models here.

class Document(models.Model):

    """Document model."""

    document_name = models.EmailField(unique=True, null=False)
    company_id = models.CharField(max_length=30, null=True)
    owner_id = models.CharField(max_length=30, null=True)
    can_view = models.CharField(max_length=30, null=True)
    can_edit = models.CharField(max_length=30, null=True)
    can_delete = models.CharField(max_length=128, blank=True)
    date_last_edited = models.DateTimeField(auto_now_add=True)
    last_edited_by = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    

    

    class Meta:
        verbose_name = "Document"
        verbose_name_plural = "Documents"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Document_detail", kwargs={"pk": self.pk})


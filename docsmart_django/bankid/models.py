from django.db import models


# Create your models here.
from company.models import Company
from customer.models import Customer
from documents.models import Document


class SignedDocuments(models.Model):

    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING, db_column='company', null=True, blank=True)
    document = models.ForeignKey(Document, on_delete=models.DO_NOTHING, db_column='document', null=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, db_column='customer', null=True, blank=True)

    updated_at = models.DateTimeField(auto_now=True, null=True)
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True, null=True)
    ip_address = models.CharField(max_length=10)

    data = models.JSONField(null=True)

    class Meta:
        db_table = 'signed_documents'
        ordering = ['-created_at']

    def __str__(self):
        return '{} - {}'.format(self.document, self.created_at)
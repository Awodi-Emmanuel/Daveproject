from django.db import models

# Create your models here.
from company.models import Company


class Payment(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, db_column='company')
    provider_name = models.CharField(max_length=500, null=True, blank=True)
    payment_id = models.CharField(max_length=500, null=True, blank=True)
    currency = models.CharField(max_length=20, null=True, blank=True)
    vat = models.IntegerField(null=True, blank=True)
    vat_amount = models.FloatField(null=True, blank=True)
    amount = models.FloatField(null=True, blank=True)
    failure_reason = models.CharField(max_length=250, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Payment"
        verbose_name_plural = "Payments"
        db_table = 'payment'
        ordering = ['-created_at']
        unique_together = ("company", "amount", "currency")

    def __str__(self):
        return '{} - {} - {}'.format(self.company, self.provider_name, self.created_at)

    def get_absolute_url(self):
        return reverse("Payment_detail", kwargs={"pk": self.pk})

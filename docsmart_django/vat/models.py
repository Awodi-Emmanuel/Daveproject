from django.db import models


# Create your models here.
from vat.manager import VATManager


class VAT(models.Model):
    name = models.CharField(verbose_name="Name", max_length=500)
    rate = models.DecimalField(verbose_name="Rate", max_digits=9, decimal_places=3)
    percentage = models.DecimalField(verbose_name="Percentage", max_digits=9, decimal_places=3)

    REQUIRED_FIELDS = ['subject', 'category', 'content']

    objects = VATManager()

    class Meta:
        verbose_name = "VAT"
        verbose_name_plural = "VATs"

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("VAT_detail", kwargs={"pk": self.pk})

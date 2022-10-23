from django.db import models
from .manager import LinesManager
from company.models import Company
from user.models import User


# Create your models here.


class Lines(models.Model):
    title = models.CharField(verbose_name="Title", max_length=500, null=True)
    item_number = models.CharField(verbose_name="Item Number", max_length=500, null=True)
    item_description = models.CharField(verbose_name="Item Description", max_length=500, null=True)
    item_type = models.CharField(verbose_name="Item Type", max_length=1000, null=True)
    related_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    related_company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    item_manufacturer_id = models.CharField(verbose_name="Item Manufacturer ID", max_length=500, null=True)
    item_quantity = models.IntegerField(verbose_name="Item Quantity")

    REQUIRED_FIELDS = ['title', 'item_number', 'item_description', 'item_type', 'item_quantity']

    objects = LinesManager()

    class Meta:
        verbose_name = "Line"
        verbose_name_plural = "Lines"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Lines_detail", kwargs={"pk": self.pk})

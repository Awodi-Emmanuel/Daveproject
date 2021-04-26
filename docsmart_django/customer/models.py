from django.db import models


# Create your models here.
from customer.manager import CustomerManager


class Customer(models.Model):

    first_name = models.CharField(verbose_name="first_name", max_length=500, null=True)
    last_name = models.CharField(verbose_name="last_name", max_length=254, null=True)
    email = models.EmailField(verbose_name='Email', null=True)
    company_name = models.CharField(verbose_name="company_name", max_length=500, null=True)
    company_number = models.CharField(verbose_name="company_number", max_length=500, null=True)
    company_address = models.CharField(verbose_name="company_address", max_length=1000,null=True)
    country = models.CharField(verbose_name="country", max_length=500,null=True)

    REQUIRED_FIELDS = ['email']

    objects = CustomerManager()

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    def __str__(self):
        return str(self.email)

    def get_absolute_url(self):
        return reverse("FAQ_detail", kwargs={"pk": self.pk})


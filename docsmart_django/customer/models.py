from django.db import models


# Create your models here.
from customer.manager import CustomerManager
from company.models import Company
from user.models import User


class Customer(models.Model):

    first_name = models.CharField(verbose_name="First Name", max_length=500, null=True)
    last_name = models.CharField(verbose_name="Last Name", max_length=254, null=True)
    email = models.EmailField(verbose_name='Email', null=True)
    related_user= models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    related_company= models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    company_email = models.EmailField(verbose_name='Company Email', null=True)
    refernce = models.CharField(verbose_name="Reference", max_length=500,null=True)
    company_name = models.CharField(verbose_name="Comapny Name", max_length=500, null=True)
    company_number = models.CharField(verbose_name="Company Number", max_length=500, null=True)
    company_address = models.CharField(verbose_name="Company Address", max_length=1000,null=True)
    company_zipcode = models.CharField(verbose_name="Company Zipcode", max_length=1000,null=True)
    company_city = models.CharField(verbose_name="Company City", max_length=1000,null=True)
    company_country = models.CharField(verbose_name="Company Country", max_length=500,null=True)
    

    REQUIRED_FIELDS = ['email']

    objects = CustomerManager()

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    def __str__(self):
        return str(self.email)

    def get_absolute_url(self):
        return reverse("Customer_detail", kwargs={"pk": self.pk})


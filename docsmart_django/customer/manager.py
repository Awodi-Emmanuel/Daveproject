from django.db import models


class CustomerManager(models.Manager):
    """
    custom company model

    first_name = models.CharField(verbose_name="First Name", max_length=500, null=True)
    last_name = models.CharField(verbose_name="Last Name", max_length=254, null=True)
    email = models.EmailField(verbose_name='Email', null=True)
    company_email = models.EmailField(verbose_name='Company Email', null=True)
    refernce = models.CharField(verbose_name="Reference", max_length=500,null=True)
    company_name = models.CharField(verbose_name="Comapny Name", max_length=500, null=True)
    company_number = models.CharField(verbose_name="Company Number", max_length=500, null=True)
    company_address = models.CharField(verbose_name="Company Address", max_length=1000,null=True)
    company_zipcode = models.CharField(verbose_name="Company Zipcode", max_length=1000,null=True)
    company_city = models.CharField(verbose_name="Company City", max_length=1000,null=True)
    company_country = models.CharField(verbose_name="Company Country", max_length=500,null=True)
    """

    def create_customer(
            self,
            first_name='',
            last_name='',
            email='',
            related_company='',
            company_email='',
            company_name='',
            company_number='',
            company_address='',
            company_zipcode='',
            company_city='',
            company_country=''
    ):
        customer = self.model(
            first_name=first_name,
            last_name=last_name,
            email=email,
            related_company=related_company,
            company_email=company_email,
            company_name=company_name,
            company_number=company_number,
            company_address=company_address,
            company_zipcode=company_zipcode,
            company_city=company_city,
            company_country=company_country
        )

        customer.save(using=self._db)
        return customer

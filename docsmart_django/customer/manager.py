from django.db import models


class CustomerManager(models.Manager):
    """
    custom company model
    """

    def create_customer(
            self,
            first_name='',
            last_name='',
            email='',
            company_name='',
            company_number='',
            company_address='',
            country=''
    ):
        customer = self.model(
            first_name=first_name,
            last_name=last_name,
            email=email,
            company_name=company_name,
            company_number=company_number,
            company_address=company_address,
            country=country
        )

        customer.save(using=self._db)
        return customer

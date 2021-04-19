"""Company manager model module"""
from django.db import models


class CompanyManager(models.Manager):
    """ 
    custom company model
    """

    def create_company(
            self,
            company_email,
            company_name,
            company_phone="",
            company_address="",
            company_state="",
            company_country="",

    ):
        """Create company."""
        if not company_email:
            raise ValueError('Company must have an email address')
        if not company_name:
            raise ValueError('Company must have a name')
        company = self.model(
            company_email=company_email.lower(),
            company_name=company_name.lower(),
            company_phone=company_phone,
            company_address=company_address,
            company_state=company_state,
            company_country=company_country,
        )

        company.save(using=self._db)
        return company

from django.db import models


class SalesManager(models.Manager):
    """
    custom sales model
    """

    def create_sales_offer(
            self,
            title='',
            status='',
            total='',
            discount='',
            vat='',
            signature_type='',
            currency='',
            customer='',
            owner='',
            company='',
            payment_schedule='',
            document='',
    ):
        sales_offer = self.model(
            title=title,
            status=status,
            total=total,
            discount=discount,
            vat=vat,
            signature_type=signature_type,
            currency=currency,
            customer=customer,
            owner=owner,
            company=company,
            payment_schedule=payment_schedule,
            document=document
        )

        sales_offer.save(using=self._db)
        return sales_offer

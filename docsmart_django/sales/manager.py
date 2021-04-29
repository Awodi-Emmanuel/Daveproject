from django.db import models

class SalesManager(models.Manager):
    """
    custom sales model
    """

    def create_sales_offer(
            self,
            title=None,
            status="Draft",
            total=None,
            discount=None,
            vat=None,
            signature_type="Bank ID",
            currency="Krona",
            owner=None,
            company=None,
            payment_schedule=None,
            document=None,
    ):
        sales_offer = self.model(
            title=title,
            status=status,
            total=total,
            discount=discount,
            vat=vat,
            signature_type=signature_type,
            currency=currency,
            owner=owner,
            company=company,
            payment_schedule=payment_schedule,
            document=document
        )

        sales_offer.save(using=self._db)
        return sales_offer

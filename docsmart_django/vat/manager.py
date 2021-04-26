from django.db import models


class VATManager(models.Manager):
    """
    custom company model
    """

    def create_vat(
            self,
            name,
            rate,
            percentage,
    ):
        vat = self.model(
            name=name,
            rate=rate,
            percentage=percentage,
        )

        vat.save(using=self._db)
        return vat

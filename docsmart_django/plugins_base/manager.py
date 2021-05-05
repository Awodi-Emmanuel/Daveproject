"""Company manager model module"""
from django.db import models


class PluginManager(models.Manager):
    """ 
    app = models.CharField(
        max_length=5,
        choices=[(tag, tag.value) for tag in APP_TYPES]
    )
    status = models.CharField(
        max_length=5,
        choices=[(tag, tag.value) for tag in STATUS], default = STATUS.TRIAL
    )
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True)
    last_payment_date = models.DateTimeField(null = True)
    next_expiry_date = models.DateTimeField(null = True)
    last_expiry_date = models.DateTimeField(null = True)

    """

    def add_plugin(
            self,
            app,
            status,
            company,
            last_payment_date,
            next_expiry_date=None,
            last_expiry_date=None
    ):

        plugin = self.model(
            app=app,
            status=status,
            company=company,
            last_payment_date=last_payment_date,
            next_expiry_date=next_expiry_date,
            last_expiry_date=last_expiry_date
        )

        plugin.save(using=self._db)
        return plugin

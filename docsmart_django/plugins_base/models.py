from django.db import models
from enum import Enum
from .manager import PluginManager
from company.models import Company
from user.models import User

# Create your models here.


class APP_TYPES(Enum):
    SALES = "Sales"
    HR = "Human resource"
    LEGAL = "Legal"
    GENERAL = "General"

class STATUS(Enum):
    ACTIVE = "Active"
    EXPIRED = "Expired"
    TRIAL = "Trial"
    EXTENSION = "Extension"


class Plugin(models.Model):


    app = models.CharField(
        max_length=100,
        choices=[(tag, tag.value) for tag in APP_TYPES]
    )
    status = models.CharField(
        max_length=100,
        choices=[(tag, tag.value) for tag in STATUS], default = STATUS.TRIAL
    )
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True)
    users = models.ManyToManyField(User, verbose_name="Permission", blank=True)
    last_payment_date = models.DateTimeField(null = True)
    next_expiry_date = models.DateTimeField(null = True)
    last_expiry_date = models.DateTimeField(null = True)


    REQUIRED_FIELDS = ['app', 'company', 'status']

    objects = PluginManager()

    class Meta:
        verbose_name = "Plugin"
        verbose_name_plural = "Plugins"

    def __str__(self):
        return self.app

    def get_absolute_url(self):
        return reverse("Plugin_detail", kwargs={"pk": self.pk})

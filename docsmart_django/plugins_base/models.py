
from django.db import models
from enum import Enum
from .manager import PluginManager
from company.models import Company
from user.models import User
from billing.models import Subscription


# Create your models here.
class AppTypes(Enum):
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
        choices=[(tag, tag.value) for tag in AppTypes]
    )
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True)
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE, blank=True)
    users = models.ManyToManyField(User, verbose_name="users", blank=True)

    REQUIRED_FIELDS = ['app', 'company', 'status']

    objects = PluginManager()

    @classmethod
    def grant_plugin_access(cls, user, plugin):
        plugin.users.add(user)

    @classmethod
    def revoke_plugin_access(cls, user, plugin):
        plugin.users.remove(user)

    class Meta:
        verbose_name = "Plugin"
        verbose_name_plural = "Plugins"

    def __str__(self):
        return self.app

    def get_absolute_url(self):
        return reverse("Plugin_detail", kwargs={"pk": self.pk})

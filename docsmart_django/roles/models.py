from django.db import models
from enum import Enum
from .manager import RolesManager
from user.models import User

# Create your models here.


class Roles(Enum):
    OWNER = "Owner"
    ADMIN = "Admin"
    EMPLOYEE = "Employee"


class Role(models.Model):
    role = models.CharField(
        max_length=5,
        choices=[(tag, tag.value) for tag in Roles]
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    company = models.ForeignKey('company.Company', on_delete=models.CASCADE, blank=True)

    REQUIRED_FIELDS = ['role', 'user', ]

    objects = RolesManager()

    # @classmethod
    # def grant_role(cls, user, company):
    #     company.user.add(user)
    #
    # @classmethod
    # def revoke_role(cls, user, company):
    #     company.user.remove(user)

    class Meta:
        verbose_name = "Role"
        verbose_name_plural = "Roles"

    def __str__(self):
        return self.role

    def get_absolute_url(self):
        return reverse("Role_detail", kwargs={"pk": self.pk})

from django.db import models
from roles.models import Role
from .manager import CompanyManager


class Company(models.Model):
    company_name = models.CharField(verbose_name="Company Name", max_length=50, unique=True)
    company_number = models.CharField(verbose_name="Company Number", max_length=254, unique=True)
    company_email = models.EmailField(verbose_name="Company Email", max_length=254, null=True)
    company_address = models.CharField(verbose_name="Company Address", max_length=200, null=True)
    company_country = models.CharField(verbose_name="Company Country", max_length=50, null=True)
    company_state = models.CharField(verbose_name="Company State", max_length=50, null=True)
    company_phone = models.CharField(verbose_name="Company Phone", max_length=20, null=True)
    user = models.ManyToManyField("user.User", verbose_name="User", blank=True)
    role = models.ManyToManyField(Role, verbose_name="Role", blank=True)

    REQUIRED_FIELDS = ['company_name', 'company_email', ]

    objects = CompanyManager()

    @classmethod
    def add_to_company(cls, user, company):
        company.user.add(user)


    @classmethod
    def remove_from_company(cls, user, company):
        company.user.remove(user)


    @classmethod
    def assign_role(cls, role, company):
        company.role.add(role)

    @classmethod
    def remove_role(cls, role, company):
        company.role.remove(role)


    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"


    def __str__(self):
        return str(self.id)


    def get_absolute_url(self):
        return reverse("Company_detail", kwargs={"pk": self.pk})

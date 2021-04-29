from enum import Enum

from django.db import models

from company.models import Company
from customer.models import Customer
from documents.models import Document
from payment_schedule.models import PaymentSchedule
from sales.manager import SalesManager
from sale_lines.models import Lines
from user.models import User
from vat.models import VAT


class Status(Enum):
    DRAFT = "Draft"
    ACCEPTED = "Accepted"
    IN_PROGRESS = "In Progress"
    REJECTED = "Rejected"


class SignatureType(Enum):
    NORMAL = "Normal"
    BANK_ID = "Bank ID"


class Currency(Enum):
    KRN = "Krona"
    EUR = "Euros"


class Sales(models.Model):
    title = models.CharField(verbose_name="title", max_length=500)
    # template = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    status = models.CharField(
        max_length=200,
        choices=[(tag, tag.value) for tag in Status], default=Status.DRAFT
    )
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=3, null=True)
    discount = models.DecimalField(default=0.00, max_digits=9, decimal_places=3, null=True)
    vat = models.ForeignKey(VAT, on_delete=models.CASCADE, blank=True, null=True)
    signature_type = models.CharField(
        max_length=200,
        choices=[(tag, tag.value) for tag in SignatureType], default=SignatureType.BANK_ID
    )
    currency = models.CharField(
        max_length=5,
        choices=[(tag, tag.value) for tag in Currency], default=Currency.KRN,
    )
    customer = models.ManyToManyField(Customer, verbose_name="Customer", blank=True)
    lines = models.ManyToManyField(Lines, verbose_name="Lines", blank=True)
    

    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    payment_schedule = models.ForeignKey(PaymentSchedule, on_delete=models.CASCADE, blank=True, null=True)
    document = models.ForeignKey(Document, on_delete=models.CASCADE, blank=True, null=True)

    REQUIRED_FIELDS = ['title', 'total', 'owner']

    objects = SalesManager()

    class Meta:
        verbose_name = "Sale"
        verbose_name_plural = "Sales"

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse("Sales_detail", kwargs={"pk": self.pk})

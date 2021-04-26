from django.db import models


# Create your models here.
from payment_schedule.manager import PaymentScheduleManager


class PaymentSchedule(models.Model):

    item = models.CharField(verbose_name="item", max_length=500)
    price = models.DecimalField(verbose_name="price", max_digits=9, decimal_places=3)
    start = models.DateTimeField(verbose_name="start")
    finish = models.DateTimeField(verbose_name="finish")

    REQUIRED_FIELDS = ['item', 'price', 'start', 'finish']

    objects = PaymentScheduleManager()

    class Meta:
        verbose_name = "PaymentSchedule"
        verbose_name_plural = "PaymentSchedules"

    def __str__(self):
        return str(self.item)

    def get_absolute_url(self):
        return reverse("Schedule_detail", kwargs={"pk": self.pk})

from django.db import models

# Create your models here.

class Payment(models.Model):

    

    class Meta:
        verbose_name = "Payment"
        verbose_name_plural = "Payments"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Payment_detail", kwargs={"pk": self.pk})

from django.db import models

# Create your models here.

class Bills(models.Model):

    

    class Meta:
        verbose_name = "Bills"
        verbose_name_plural = "Billss"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Bills_detail", kwargs={"pk": self.pk})


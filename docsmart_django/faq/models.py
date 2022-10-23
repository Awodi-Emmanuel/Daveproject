from django.db import models
from .manager import FAQManager
from mdeditor.fields import MDTextField


class FAQ(models.Model):
    subject = models.CharField(verbose_name="Subject", max_length=500)
    category = models.CharField(verbose_name="Category", max_length=254)
    content = MDTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ['subject', 'category', 'content']

    objects = FAQManager()

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"

    def __str__(self):
        return str(self.subject)

    def get_absolute_url(self):
        return reverse("FAQ_detail", kwargs={"pk": self.pk})

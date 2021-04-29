from django.db import models
from .manager import NotificationsManager
from mdeditor.fields import MDTextField
from user.models import User


class Notification(models.Model):

    subject = models.CharField(verbose_name="Subject", max_length=500)
    content = MDTextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="User")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ['subject', 'content', 'user']

    objects = NotificationsManager()

    class Meta:
        verbose_name = "Notification"
        verbose_name_plural = "Notifications"

    def __str__(self):
        return str(self.subject)

    def get_absolute_url(self):
        return reverse("Notification_detail", kwargs={"pk": self.pk})

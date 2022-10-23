from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from user.models import User
from .manager import LogsManager


class Logs(models.Model):

    performed_by = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, related_name='performed_bu')
    loggable = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('loggable', 'object_id')
    affected_user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, related_name='affected_user')
    action = models.CharField(verbose_name="Action", max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ['performed_by', 'action']

    objects = LogsManager()

    class Meta:
        verbose_name = "Log"
        verbose_name_plural = "Logs"

    def __str__(self):
        return str(self.action)

    def get_absolute_url(self):
        return reverse("Log_detail", kwargs={"pk": self.pk})

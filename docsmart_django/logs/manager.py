from django.db import models


class LogsManager(models.Manager):
    """
    custom log model
    """

    """
        performed_by = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, related_name='performed_bu')
        loggable = models.ForeignKey(ContentType, on_delete=models.CASCADE)
        object_id = models.PositiveIntegerField()
        content_object = GenericForeignKey('loggable', 'object_id')
        affected_user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, related_name='affected_user')
        action = models.CharField(verbose_name="Action", max_length=500)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
    """

    def create_log(
            self,
            performed_by,
            affected_user,
            loggable,
            action,
    ):
        log = self.model(
            performed_by=performed_by,
            affected_user=affected_user,
            loggable=loggable,
            action=action,
        )

        log.save(using=self._db)
        return log

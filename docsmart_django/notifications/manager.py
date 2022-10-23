from django.db import models


class NotificationsManager(models.Manager):
    """
    custom company model
    """

    def create_notification(
            self,
            subject,
            user,
            content,
    ):
        notification = self.model(
            subject=subject,
            user=user,
            content=content,
        )

        notification.save(using=self._db)
        return notification

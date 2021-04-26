from django.db import models


class PaymentScheduleManager(models.Manager):
    """
    custom company model
    """

    def create_schedule(
            self,
            item,
            price,
            start,
            finish
    ):
        schedule = self.model(
            item=item,
            price=price,
            start=start,
            finish=finish
        )

        schedule.save(using=self._db)
        return schedule

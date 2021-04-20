from django.db import models


class FAQManager(models.Manager):
    """
    custom company model
    """

    def create_faq(
            self,
            subject,
            category,
            content,
    ):
        faq = self.model(
            subject=subject,
            category=category,
            content=content,
        )

        faq.save(using=self._db)
        return faq

"""Company manager model module"""
from django.db import models


class PluginManager(models.Manager):

    def add_plugin(
            self,
            app,
            subscription,
            company,
    ):

        plugin = self.model(
            app=app,
            subscription=subscription,
            company=company,
        )

        plugin.save(using=self._db)
        return plugin

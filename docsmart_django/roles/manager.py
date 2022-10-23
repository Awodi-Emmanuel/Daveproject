"""Company manager model module"""
from django.db import models


class RolesManager(models.Manager):
    """ 
    custom company model
    """

    def assign_role(
            self,
            role,
            user,
            company
            

    ):
        """Create company."""
        if not role:
            raise ValueError('Role cannot be empty')
        if not user:
            raise ValueError('user cannot be empty')
        roles = self.model(
            role=role,
            user=user,
            company=company
        )

        roles.save(using=self._db)
        return roles

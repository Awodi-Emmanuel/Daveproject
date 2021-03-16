"""User manager model module"""
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """ 
    custom user model
    """
    def create_user(
            self,
            first_name,
            last_name,
            phone,
            email,
            password,
            is_active=False,
            is_staff=False,
            is_admin=False
        ):
        """Create user."""
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email))
        user.is_active=is_active
        user.is_staff=is_staff
        user.is_admin=is_admin
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """Create a superuser."""
        return self.create_user(
            email,
            password,
            is_active=True,
            is_staff=True,
            is_admin=True
        )
"""User manager model module"""
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth import get_user_model
from company.company_manager import CompanyManager
from company.models import Company
import django.db.transaction


class UserManager(BaseUserManager):
    """ 
    custom user model
    """
    def create_user(
            self,
            first_name="",
            last_name="",
            phone="",
            email="",
            password="",
            is_active=False,
            is_staff=False,
            is_admin=False
        ):
        """Create user."""
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            phone = phone,   
        )

        user.is_active=is_active
        user.is_staff=is_staff
        user.is_admin=is_admin
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_default_user(
            self,
            email="",
            is_active=False,
            is_staff=False,
            is_admin=False
        ):
        """Create default user."""
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(

            email=self.normalize_email(email),

        )
        user.is_active=is_active
        user.is_staff=is_staff
        user.is_admin=is_admin
        user.save(using=self._db)
        return user

    def complete_user_onboarding(
            self,
            first_name="",
            last_name="",
            phone="",
            email="",
            password="",
            company_name="",
            company_email="",
            is_active=True,
            is_staff=False,
            is_admin=False
        ):
        """complete user onboarding."""

        if not email:
            raise ValueError('Users must pass an email address')
        if not first_name:
            raise ValueError('Users must pass first_name')
        if not last_name:
            raise ValueError('Users must pass last_name')
        if not phone:
            raise ValueError('Users must pass phone number')
        if not password:
            raise ValueError('Users must enter password')

        user_model = get_user_model()
        try:

            user = user_model.objects.get(email=email)
            user.first_name = first_name
            user.last_name = last_name
            user.phone = phone
            user.is_active=is_active
            user.is_staff=is_staff
            user.is_admin=is_admin
            user.set_password(password)
            user.save()
            return user

        except user_model.DoesNotExist:

            raise ValueError('User does not exist')

        else:
            return None

    def create_superuser(self, email, password):
        """Create a superuser."""
        return self.create_user(
            email,
            password,
            is_active=True,
            is_staff=True,
            is_admin=True
        )
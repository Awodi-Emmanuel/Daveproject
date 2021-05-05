import jwt
from rest_framework import authentication, exceptions
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from company.models import Company
from .models import Plugin, STATUS


class PluginsAthorization(authentication.BaseAuthentication):

    def authenticate(self, request, user=None, plugin=None):

        user = request.user

        try:
            
            company = Company.objects.get(user__id= user.id)
            plugin = Plugin.objects.get(company = company.id, app=plugin, users__user_id = user.id)


            if plugin.status == STATUS.ACTIVE:
                
                return plugin

            raise exceptions.AuthenticationFailed(
                'You do not have access to this plugin')



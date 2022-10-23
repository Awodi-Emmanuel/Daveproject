from company.models import Company
from .models import Plugin, AppTypes
from rest_framework import permissions
from django.core.exceptions import ObjectDoesNotExist


def check_plugin_from_path(uri):
    keyword = 'api/'
    before_keyword, keyword, after_keyword = uri.partition(keyword)
    path = after_keyword.split('/')
    return path[0]


class CompanyPluginAccessPermission(permissions.BasePermission):
    """
    Global permission check for plugin access
    """
    message = 'Your company does not have access to this plugin'

    def has_permission(self, request, view):
        try:
            app = check_plugin_from_path(request.get_full_path())
            company = Company.objects.get(user__id=request.user.id)
            plugin = Plugin.objects.get(company=company.id, app=app)
            return plugin.subscription.status
        except ObjectDoesNotExist:
            try:
                company = Company.objects.get(user__id=request.user.id)
                plugin = Plugin.objects.get(company=company.id, app=AppTypes.GENERAL.value)
                return plugin.subscription.status
            except ObjectDoesNotExist:
                return False


class UserPluginAccessPermission(permissions.BasePermission):
    """
    Global permission check for plugin access
    """
    message = 'You do not have access to this plugin'

    def has_permission(self, request, view):
        try:
            app = check_plugin_from_path(request.get_full_path())
            company = Company.objects.get(user__id=request.user.id)
            plugin = Plugin.objects.get(company=company.id, app=app, users__id=request.user.id)
            return plugin.subscription.status
        except ObjectDoesNotExist:
            try:
                company = Company.objects.get(user__id=request.user.id)
                plugin = Plugin.objects.get(company=company.id, app=AppTypes.GENERAL.value, users__id=request.user.id)
                return plugin.subscription.status
            except ObjectDoesNotExist:
                return False


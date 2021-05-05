from company.models import Company
from .models import Plugin, STATUS
from rest_framework import permissions
from roles.models import Role, Roles

class PluginAccessPermission(permissions.BasePermission):
    """
    Global permission check for plugin access
    """
    message = 'Company does not have access to this plugin'

    def has_permission(self, request, view):

        app = request.data.get('app')
        company = Company.objects.get(user__id = request.user.id)
        plugin = Plugin.objects.get(company = company.id, app=app)

        return plugin.status == STATUS.ACTIVE.value

                



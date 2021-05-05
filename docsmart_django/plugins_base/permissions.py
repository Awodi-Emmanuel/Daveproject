from rest_framework import permissions
from company.models import Company
from .models import Plugin, STATUS

class BlocklistPermission(permissions.BasePermission):
    """
    Global permission check for blocked IPs.
    """

    def has_permission(self, request, view, plugin=None):

        user = request.user
        try:
            
            company = Company.objects.get(user__id= user.id)
            plugin = Plugin.objects.get(company = company.id, app=plugin, users__user_id = user.id)


            if plugin.status == STATUS.ACTIVE:
                
                return True

            return False
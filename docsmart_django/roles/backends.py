from company.models import Company
from rest_framework import permissions
from roles.models import Role, Roles


class OwnerPermission(permissions.BasePermission):
    """
    Global permission check for company ownership
    """
    message = 'You cannot perform this action'

    def has_permission(self, request, view):
        company = Company.objects.get(user__id=request.user.id)
        role = Role.objects.get(user_id=request.user.id, company=company.id)
        return role.role == Roles.OWNER.value

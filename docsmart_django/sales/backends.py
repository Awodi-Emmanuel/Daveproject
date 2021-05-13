from rest_framework import permissions
from django.core.exceptions import ObjectDoesNotExist

from sales.models import Sales


class OwnsSalesOffer(permissions.BasePermission):
    """
    Global permission check for plugin access
    """
    message = 'You do not own this offer'

    def has_permission(self, request, view):
        try:
            Sales.objects.get(id=request.GET.get('offer'), owner=request.user.id)
            return True
        except ObjectDoesNotExist:
            return False

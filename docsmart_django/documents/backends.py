from rest_framework import permissions
from django.core.exceptions import ObjectDoesNotExist

from documents.models import Document
from sales.models import Sales


class CanEditDocument(permissions.BasePermission):
    """
    Global permission check for plugin access
    """
    message = 'You can not edit this document'

    def has_permission(self, request, view):
        try:
            document = Document.objects.get(id=request.GET.get('document'))
            document_permissions = document.permissions.get(user_id=request.user.id)
            return document_permissions.can_edit
        except ObjectDoesNotExist:
            return False


class CanViewDocument(permissions.BasePermission):
    """
    Global permission check for plugin access
    """
    message = 'You can not edit this document'

    def has_permission(self, request, view):
        try:
            document = Document.objects.get(id=request.GET.get('document'))
            document_permissions = document.permissions.get(user_id=request.user.id)
            return document_permissions.can_view
        except ObjectDoesNotExist:
            return False


class CanDeleteDocument(permissions.BasePermission):
    """
    Global permission check for plugin access
    """
    message = 'You can not edit this document'

    def has_permission(self, request, view):
        try:
            document = Document.objects.get(id=request.GET.get('document'))
            document_permissions = document.permissions.get(user_id=request.user.id)
            return document_permissions.can_delete
        except ObjectDoesNotExist:
            return False

from django.urls import path
from .views import CreateDocument, FetchUserDocument, FetchUserFolderStructureWithPermissions


urlpatterns = [
    path('create-document', CreateDocument.as_view()),
    path('fetch-user-documents', FetchUserDocument.as_view()),
    path('fetch-user-folder-structure-with-perm', FetchUserFolderStructureWithPermissions.as_view()),
]

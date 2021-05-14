from django.urls import path
from .views import CreateDocument, FetchUserDocument, FetchUserFolderStructureWithPermissions, \
    FetchCompanyFolderStructureWithPermissions, CreateSingleUserDirectory, DeleteSingleUserDocument, \
    DeleteSingleCompanyDocument, FetchSingleUserDocument

urlpatterns = [
    path('create-document', CreateDocument.as_view()),
    path('fetch', FetchSingleUserDocument.as_view()),
    path('fetch-user-documents', FetchUserDocument.as_view()),
    path('delete-document', DeleteSingleUserDocument.as_view()),
    path('delete-company-document', DeleteSingleCompanyDocument.as_view()),
    path('create-single-user-folder', CreateSingleUserDirectory.as_view()),
    path('fetch-user-folder-structure-with-perm', FetchUserFolderStructureWithPermissions.as_view()),
    path('fetch-company-folder-structure-with-perm', FetchCompanyFolderStructureWithPermissions.as_view()),
]

from django.urls import path
from .views import CreateDocument, FetchUserDocument, FetchUserFolderStructureWithPermissions, CreateSingleUserDirectory

urlpatterns = [
    path('create-document', CreateDocument.as_view()),
    path('fetch-user-documents', FetchUserDocument.as_view()),
    path('create-single-folder', CreateSingleUserDirectory.as_view()),
    path('fetch-user-folder-structure-with-perm', FetchUserFolderStructureWithPermissions.as_view()),
]

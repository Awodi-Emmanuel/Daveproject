from django.urls import path
from .views import CreateDocument, FetchUserDocument, FetchUserFolders, FetchUserFolderStructureWithPermissions


urlpatterns = [
    path('create-document', CreateDocument.as_view()),
    path('fecth-user-documents', FetchUserDocument.as_view()),
    path('fecth-user-folders', FetchUserFolders.as_view()),
    path('fecth-user-folder-structer-with-perm', FetchUserFolderStructureWithPermissions.as_view()),
]
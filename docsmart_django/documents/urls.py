from django.urls import path
from .views import CreateDocument, FetchDocument, FetchUserFolders


urlpatterns = [
    path('create-document', CreateDocument.as_view()),
    path('fecth-user-documents', FetchDocument.as_view()),
    path('fecth-user-folders', FetchUserFolders.as_view()),
]
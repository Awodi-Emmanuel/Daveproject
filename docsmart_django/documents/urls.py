from django.urls import path
from .views import CreateDocument


urlpatterns = [
    path('create-document', CreateDocument.as_view()),
    
]
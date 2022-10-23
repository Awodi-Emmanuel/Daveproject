from django.urls import path
from .views import SignDocument, CollectStatus

urlpatterns = [
    path('sign', SignDocument.as_view()),
    path('check-status', CollectStatus.as_view()),
]

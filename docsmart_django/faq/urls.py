from django.urls import path
from .views import FetchFAQ

urlpatterns = [
    path('fetch', FetchFAQ.as_view()),
]

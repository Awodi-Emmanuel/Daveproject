from django.urls import path
from .views import UpdateCompany

urlpatterns = [
    path('fetch', UpdateCompany.as_view()),
]

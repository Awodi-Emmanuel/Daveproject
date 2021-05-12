
from django.urls import path
from .views import CreateSalesOffer, RetrieveSalesOffer, UpdateSalesOffer

urlpatterns = [
    path('create', CreateSalesOffer.as_view()),
    path('fetch', RetrieveSalesOffer.as_view()),
    path('update', UpdateSalesOffer.as_view()),
]

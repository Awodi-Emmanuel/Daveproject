
from django.urls import path
from .views import CreateSalesOffer, RetrieveSalesOffer, UpdateSalesOffer, RetrieveSingleSalesOffer, AddCustomersToOffer

urlpatterns = [
    path('create', CreateSalesOffer.as_view()),
    path('fetch', RetrieveSalesOffer.as_view()),
    path('add_customer', AddCustomersToOffer.as_view()),
    path('fetch_offer', RetrieveSingleSalesOffer.as_view()),
    path('update', UpdateSalesOffer.as_view()),
]

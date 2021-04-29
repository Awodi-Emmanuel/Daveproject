
from django.urls import path
from .views import CreateSalesOffer, RetrieveSalesOffer


urlpatterns = [
    path('create', CreateSalesOffer.as_view()),
    path('fetch', RetrieveSalesOffer.as_view()),
]
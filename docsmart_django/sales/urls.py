
from django.urls import path
from .views import CreateSalesOffer


urlpatterns = [
    path('create', CreateSalesOffer.as_view()),
]
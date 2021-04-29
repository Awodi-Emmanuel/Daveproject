
from django.urls import path
from .views import CreateCustomer


urlpatterns = [
    path('create', CreateCustomer.as_view()),
    # path('fetch', RetrieveSalesOffer.as_view()),
]
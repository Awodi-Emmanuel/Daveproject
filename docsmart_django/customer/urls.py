
from django.urls import path
from .views import CreateCustomer, FetchCustomers


urlpatterns = [
    path('create', CreateCustomer.as_view()),
    path('fetch', FetchCustomers.as_view()),
]
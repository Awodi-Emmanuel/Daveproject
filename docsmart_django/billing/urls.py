
from django.urls import path
from .views import GetHostedPage, FetchPlans


urlpatterns = [
    path('hosted-page', GetHostedPage.as_view()),
    path('fetch-plans', FetchPlans.as_view()),
]
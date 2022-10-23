
from django.urls import path
from .views import AddPlugin, AddUserToPlugin


urlpatterns = [
    path('add', AddPlugin.as_view()),
    path('add-user', AddUserToPlugin.as_view()),
]
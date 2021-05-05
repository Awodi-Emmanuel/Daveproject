
from django.urls import path
from .views import AddPlugin


urlpatterns = [
    path('add', AddPlugin.as_view()),
    # path('fetch', FetchLines.as_view()),
]
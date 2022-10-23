
from django.urls import path
from .views import CreateLines, FetchLines


urlpatterns = [
    path('create', CreateLines.as_view()),
    path('fetch', FetchLines.as_view()),
]
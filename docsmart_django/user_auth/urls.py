
from django.urls import path
from .views import RegisterView, LoginView, SignUp


urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('signup', SignUp.as_view()),
    
]
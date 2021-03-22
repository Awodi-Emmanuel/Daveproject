
from django.urls import path
from .views import RegisterView, LoginView, SignUp, InviteUser


urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('signup', SignUp.as_view()),
    path('invite', InviteUser.as_view()),
    
]
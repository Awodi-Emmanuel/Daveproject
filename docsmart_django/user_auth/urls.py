
from django.urls import path
from .views import CompleteUserSignUp, LoginView, SignUp, InviteUser, CompleteRegistrationForInvite


urlpatterns = [
    path('complete-signup', CompleteUserSignUp.as_view()),
    path('login', LoginView.as_view()),
    path('signup', SignUp.as_view()),
    path('invite', InviteUser.as_view()),
    path('complete-invite', CompleteRegistrationForInvite.as_view()),
    
]
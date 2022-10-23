
from django.urls import path
from .views import CompleteUserSignUp, LoginView, SignUp, InviteUser, CompleteRegistrationForInvite, \
    ChangePasswordView, RequestPasswordResetEmail, PasswordTokenCheckAPI, SetNewPasswordAPIView, Register


urlpatterns = [
    path('complete-signup', CompleteUserSignUp.as_view()),
    path('login', LoginView.as_view()),
    path('signup', SignUp.as_view()),
    path('register', Register.as_view()),
    path('invite', InviteUser.as_view()),
    path('change_password', ChangePasswordView.as_view()),
    path('complete-invite', CompleteRegistrationForInvite.as_view()),
    path('request-reset-email/', RequestPasswordResetEmail.as_view(),
         name="request-reset-email"),
    path('password-reset/<uidb64>/<token>/',
         PasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),
    path('password-reset-complete', SetNewPasswordAPIView.as_view(),
         name='password-reset-complete')
]
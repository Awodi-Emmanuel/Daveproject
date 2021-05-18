from rest_framework.generics import GenericAPIView, UpdateAPIView

from plugins_base.models import Plugin, AppTypes, STATUS
from roles.models import Role, Roles
from .serializers import UserSerializer, LoginSerializer, SignUpSerializer, ChangePasswordSerializer, \
    ResetPasswordEmailRequestSerializer, SetNewPasswordSerializer
from company.serializers import CompanySerializer
from rest_framework.response import Response
from django.conf import settings
from django.contrib import auth
from django.contrib.auth import get_user_model
from company.models import Company
from rest_framework import status, permissions
from user.models import User
import jwt
from .classes.email.send import SendMail
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from .helpers.utils import Util
from django.http import HttpResponsePermanentRedirect
from billing.models import Subscription, BillingPlans
from datetime import datetime, timedelta, date
import os


class CustomRedirect(HttpResponsePermanentRedirect):

    allowed_schemes = [os.environ.get('APP_SCHEME'), 'http', 'https']


class SignUp(GenericAPIView):
    serializer_class = SignUpSerializer

    @staticmethod
    def post(request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            SendMail.send_confirmation_mail(url='http://127.0.0.1:8000/api/auth/complete-signup', user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Register(GenericAPIView):
    serializer_class = UserSerializer

    @staticmethod
    def post(request):

        user_serializer = UserSerializer(data=request.data)
        company_serializer = CompanySerializer(data=request.data)

        if user_serializer.is_valid() and company_serializer.is_valid():
            user = user_serializer.save()
            company = company_serializer.save()
            Company.add_to_company(user=user, company=company)
            Role.objects.assign_role(role=Roles.OWNER.value, user=user, company=company)
            sub = Subscription.objects.create(
                company=company,
                plan=BillingPlans.objects.get(plan_id="alpha-plan"),
                billing_period=15,
                billing_period_unit='day',
                plan_amount=0,
                plan_unit_price=0,
                plan_quantity=1,
                subscription_id='Trial',
                next_billing_at=str(date.today() + timedelta(days=15)),
                created_at=str(datetime.today()),
                activated_at=str(datetime.today()),
                status=True
            )
            plugin = Plugin.objects.add_plugin(app=AppTypes.GENERAL.value, subscription=sub, company=company)
            Plugin.grant_plugin_access(user=user, plugin=plugin)
            SendMail.send_confirmation_mail(url='http://127.0.0.1:8000/api/auth/complete-signup', user=user)
            response_data = {'user_object': user_serializer.data, 'company_object': company_serializer.data}
            return Response(response_data, status=status.HTTP_201_CREATED)

        else:

            user_serializer.is_valid()
            company_serializer.is_valid()
            error_data = {'user_error': user_serializer.errors, 'company_error': company_serializer.errors}
            return Response(error_data, status=status.HTTP_400_BAD_REQUEST)


class InviteUser(GenericAPIView):
    serializer_class = SignUpSerializer

    @staticmethod
    def post(request):
        serializer = SignUpSerializer(data=request.data)

        if request.data.get('company_id') is not None or request.data.get('company_id') != '':

            if request.data.get('user_id') is None or request.data.get('user_id') == '':
                return Response({'message': "user_id field is required and must not be empty"},
                                status=status.HTTP_400_BAD_REQUEST)

            if serializer.is_valid():
                user_model = get_user_model()
                invited_user = serializer.save()
                company = Company.objects.get(id=request.data.get('company_id'))
                current_user = user_model.objects.get(id=request.data.get('user_id'))

                SendMail.send_invite(url='http://127.0.0.1:8000/api/auth/complete-signup', invited_user=invited_user,
                                     current_user=current_user)
                Company.add_to_company(user=invited_user, company=company)
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({'message': "company_id field is required and must not be empty"},
                        status=status.HTTP_400_BAD_REQUEST)


class CompleteRegistrationForInvite(GenericAPIView):
    serializer_class = UserSerializer

    @staticmethod
    def post(request):
        user_serializer = UserSerializer(data=request.data)

        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)

        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompleteUserSignUp(GenericAPIView):
    serializer_class = UserSerializer

    @staticmethod
    def post(request):

        user_serializer = UserSerializer(data=request.data)
        company_serializer = CompanySerializer(data=request.data)

        if user_serializer.is_valid() and company_serializer.is_valid():

            user_id = user_serializer.save()
            company_id = company_serializer.save()
            Company.add_to_company(user=user_id, company=company_id)

            response_data = {'user_object': user_serializer.data, 'company_object': company_serializer.data}
            return Response(response_data, status=status.HTTP_201_CREATED)

        else:

            user_serializer.is_valid()
            company_serializer.is_valid()
            error_data = {'user_error': user_serializer.errors, 'company_error': company_serializer.errors}
            return Response(error_data, status=status.HTTP_400_BAD_REQUEST)


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    @staticmethod
    def post(request):
        data = request.data
        email = data.get('email')
        password = data.get('password')
        user = auth.authenticate(username=email, password=password)

        if user:
            auth_token = jwt.encode(
                {'email': user.email}, settings.JWT_SECRET_KEY, algorithm="HS256")

            serializer = UserSerializer(user)

            data = {'user': serializer.data, 'token': auth_token}

            return Response(data, status=status.HTTP_200_OK)

        return Response({'message': 'Invalid credentials', 'status': 'failed'}, status=status.HTTP_401_UNAUTHORIZED)


class ChangePasswordView(UpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    queryset = User.objects.all()
    serializer_class = ChangePasswordSerializer


class RequestPasswordResetEmail(GenericAPIView):
    serializer_class = ResetPasswordEmailRequestSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        email = request.data.get('email', '')

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            current_site = get_current_site(
                request=request).domain
            relativeLink = reverse(
                'password-reset-confirm', kwargs={'uidb64': uidb64, 'token': token})

            redirect_url = request.data.get('redirect_url', '')
            absurl = 'http://'+current_site + relativeLink
            email_body = 'Hello, \n Use link below to reset your password  \n' + \
                absurl+"?redirect_url="+redirect_url
            data = {'email_body': email_body, 'to_email': user.email,
                    'email_subject': 'Reset your passsword'}
            Util.send_email(data)
            
        return Response({'success': 'We have sent you a link to reset your password'}, status=status.HTTP_200_OK)


class PasswordTokenCheckAPI(GenericAPIView):
    serializer_class = SetNewPasswordSerializer

    def get(self, request, uidb64, token):

        redirect_url = request.GET.get('redirect_url')

        try:
            id = smart_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                if len(redirect_url) > 3:
                    return CustomRedirect(redirect_url+'?token_valid=False')
                else:
                    return CustomRedirect(os.environ.get('FRONTEND_URL', '')+'?token_valid=False')

            if redirect_url and len(redirect_url) > 3:
                return CustomRedirect(redirect_url+'?token_valid=True&message=Credentials Valid&uidb64='+uidb64+'&token='+token)
            else:
                return CustomRedirect(os.environ.get('FRONTEND_URL', '')+'?token_valid=False')

        except DjangoUnicodeDecodeError as identifier:
            try:
                if not PasswordResetTokenGenerator().check_token(user):
                    return CustomRedirect(redirect_url+'?token_valid=False')
                    
            except UnboundLocalError as e:
                return Response({'error': 'Token is not valid, please request a new one'},
                                status=status.HTTP_400_BAD_REQUEST)


class SetNewPasswordAPIView(GenericAPIView):
    serializer_class = SetNewPasswordSerializer

    def patch(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'success': True, 'message': 'Password reset success'}, status=status.HTTP_200_OK)

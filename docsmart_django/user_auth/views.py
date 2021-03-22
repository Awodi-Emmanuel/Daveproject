from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import UserSerializer, LoginSerializer, SignUpSerializer
from company.serializers import CompanySerializer
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.contrib import auth
from django.contrib.auth import get_user_model
from company.models import Company
import jwt
# Create your views here.


class SignUp(GenericAPIView):
    
    serializer_class = SignUpSerializer

    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InviteUser(GenericAPIView):
    
    serializer_class = SignUpSerializer

    def post(self, request):
        serializer = SignUpSerializer(data=request.data)

        if request.data.get('company_id') is not None and request.data.get('company_id') != '':
            
            if serializer.is_valid():

                user_id = serializer.save()
                company =Company.objects.get(id=request.data.get('company_id'))


                Company.add_to_company(user=user_id, company=company)

                return Response(serializer.data, status=status.HTTP_201_CREATED)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({'message' : "company_id field is required and must not be empty"}, status=status.HTTP_400_BAD_REQUEST)

        
class CompleteRegistrationForInvite(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):

        user_serializer = UserSerializer(data=request.data)

        if user_serializer.is_valid():
            
            user_id = user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)

        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
class CompleteUserSignUp(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):

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

    def post(self, request):
        data = request.data
        email = data.get('email')
        password = data.get('password')
        user = auth.authenticate(username=email, password=password)

        if user:
            auth_token = jwt.encode(
                {'email': user.email}, settings.JWT_SECRET_KEY)

            serializer = UserSerializer(user)

            data = {'user': serializer.data, 'token': auth_token}

            return Response(data, status=status.HTTP_200_OK)

        return Response({'message': 'Invalid credentials','status': 'failed'}, status=status.HTTP_401_UNAUTHORIZED)
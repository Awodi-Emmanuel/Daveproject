
from rest_framework import serializers
from django.contrib.auth.models import User
from user.models import User
from company.models import Company
from company.serializers import CompanySerializer


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=65, min_length=8, write_only=True)
    email = serializers.EmailField(max_length=255, min_length=4)
    phone = serializers.CharField(max_length=30, min_length=10)
    first_name = serializers.CharField(max_length=255, min_length=2)
    last_name = serializers.CharField(max_length=255, min_length=2)
    company_email = serializers.SerializerMethodField()
    company_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone','email', 'password','company_email', 'company_name',]

    def get_company_email(self, obj):
        return obj.company_email
    
    def get_company_name(self, obj):
        return obj.company_name

    def validate(self, attrs):
        email = attrs.get('email', '')
        # company_email = attrs.get('company_email', '')
        # company_name = attrs.get('company_name', '')
        if email is None:
            raise serializers.ValidationError(
                {'email': ('Email cannot be empty')})
        if User.objects.filter(email=email).exists() == False :
            raise serializers.ValidationError(
                {'email': ('User does not exist')})
        if company_email is None:
            raise serializers.ValidationError(
                {'email': ('Company Email cannot be empty')})
        if company_name is None:
            raise serializers.ValidationError(
                {'email': ('Company Name cannot be empty')})
        if Company.objects.filter(company_email=company_email).exists():
            raise serializers.ValidationError(
                {'company_email': ('Company email is already in use')})
        if Company.objects.filter(company_name=company_name.lower()).exists():
            raise serializers.ValidationError(
                {'company_name': ('Company email is already in use')})
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.complete_user_onboarding(**validated_data)


class SignUpSerializer(serializers.ModelSerializer):
    
    email = serializers.EmailField(max_length=255, min_length=4)

    class Meta:
        model = User
        fields = ['email']

    def validate(self, attrs):
        email = attrs.get('email', '')
        if email is None:
            raise serializers.ValidationError(
                {'email': ('Email cannot be empty')})
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'email': ('Email is already in use')})
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_default_user(**validated_data)

class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=65, min_length=8, write_only=True)
    email = serializers.CharField(max_length=255, min_length=2)

    class Meta:
        model = User
        fields = ['email', 'password']
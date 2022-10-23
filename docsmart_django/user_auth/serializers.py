from abc import ABC

from rest_framework import serializers
from django.contrib.auth.models import User
from user.models import User
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=65, min_length=8, write_only=True)
    email = serializers.EmailField(max_length=255, min_length=4)
    # phone = serializers.CharField(max_length=30, min_length=10)
    first_name = serializers.CharField(max_length=255, min_length=2)
    last_name = serializers.CharField(max_length=255, min_length=2)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', ]

    def validate(self, attrs):
        email = attrs.get('email', '')

        if email is None:
            raise serializers.ValidationError(
                {'email': 'Email cannot be empty'})
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'email': 'Email is already in use'})
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class SignUpSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=4)

    class Meta:
        model = User
        fields = ['email']

    def validate(self, attrs):
        email = attrs.get('email', '')
        if email is None:
            raise serializers.ValidationError(
                {'email': 'Email cannot be empty'})
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'email': 'Email is already in use'})
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


class ChangePasswordSerializer(serializers.ModelSerializer):
    mew_password = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('old_password', 'mew_password')

    def validate(self, attrs):
        user = self.request.user
        if not user.check_password(attrs['old_password']):
            raise serializers.ValidationError({"old_password": "Old password is not correct"})
        return attrs

    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()
        return instance


class ResetPasswordEmailRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=2)

    redirect_url = serializers.CharField(max_length=500, required=False)

    class Meta:
        fields = ['email']


class SetNewPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(
        min_length=6, max_length=68, write_only=True)
    token = serializers.CharField(
        min_length=1, write_only=True)
    uidb64 = serializers.CharField(
        min_length=1, write_only=True)

    class Meta:
        fields = ['password', 'token', 'uidb64']

    def validate(self, attrs):
        try:
            password = attrs.get('password')
            token = attrs.get('token')
            uidb64 = attrs.get('uidb64')

            id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                raise AuthenticationFailed('The reset link is invalid', 401)

            user.set_password(password)
            user.save()

            return (user)
        except Exception as e:
            raise AuthenticationFailed('The reset link is invalid', 401)
        return super().validate(attrs)

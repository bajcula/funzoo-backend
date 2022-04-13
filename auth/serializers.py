from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings
from django.contrib.auth.models import update_last_login
from django.core.exceptions import ObjectDoesNotExist

from accounts.serializers import CustomUserDetailsSerializer
from accounts.models import MyUser

class LoginSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data['user'] = CustomUserDetailsSerializer(self.user).data
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data


class RegisterSerializer(CustomUserDetailsSerializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)
    email = serializers.EmailField(required=True, write_only=True, max_length=128)
    name = serializers.CharField(max_length=64, min_length=2, required=True)

    class Meta:
        model = MyUser
        fields = ['id', 'email', 'password', 'name', 'is_active']

    def create(self, validated_data):
        try:
            user = MyUser.objects.get(email=validated_data['email'])
        except ObjectDoesNotExist:
            user = MyUser.objects.create_user(**validated_data)
        return user
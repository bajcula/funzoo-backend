from wsgiref import validate
from rest_framework import serializers 
from .models import MyUser
from django.contrib.auth.hashers import make_password

class CustomUserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('email', 'name', 'password', 'id', 'last_login')
        read_only_fields = ('id',)
        
    def create(self,validated_data):
        user = MyUser(
            email=validated_data['email'],
            name=validated_data['name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
        


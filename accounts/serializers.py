from rest_framework import serializers 
from .models import MyUser

class CustomUserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('email', 'name', 'id', 'last_login')
        read_only_fields = ('email','id',)

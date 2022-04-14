from rest_framework import generics
from .serializers import CustomUserDetailsSerializer
from .models import MyUser

class MyUserList(generics.ListCreateAPIView):
    queryset = MyUser.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = CustomUserDetailsSerializer # tell django what serializer to use

class MyUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MyUser.objects.all().order_by('id')
    serializer_class = CustomUserDetailsSerializer
from rest_framework import generics

from . import serializers
from .models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view





class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserCreateList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.RegistrationSerializer


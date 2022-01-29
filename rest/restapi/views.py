from rest_framework import generics, permissions, viewsets
from . import serializers
from django.contrib.auth.models import User
from .models import User, Profile
from .serializers import ProfileSerializer





class UserList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = serializers.ProfileSerializer



from rest_framework import serializers
from django.contrib.auth.models import User
from .models import User, Profile


class ProfileSerializer(serializers.ModelSerializer):
    firstname = serializers.CharField(source='user.first_name')
    lastname = serializers.CharField(source='user.last_name')
    email = serializers.CharField(source='user.email')

    class Meta:
        model = Profile
        fields = ('firstname', 'lastname', 'email', 'date_of_birth', 'photo', 'gender')




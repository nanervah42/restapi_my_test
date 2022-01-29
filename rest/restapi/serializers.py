from rest_framework import serializers
from django.contrib.auth.models import User
from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'photo', 'date_of_birth', 'gender')


class RegistrationSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'first_name', 'last_name', 'email', 'photo', 'date_of_birth', 'gender')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def save(self):
        account = User(
            username=self.validated_data['username'],
            email=self.validated_data['email'],
            first_name=self.validated_data['first_name'],
            date_of_birth=self.validated_data['date_of_birth'],
            last_name=self.validated_data['last_name'],
            gender=self.validated_data['gender'],
            photo=self.validated_data['photo']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'passwords must match'})
        account.set_password(password)
        account.save()
        return account
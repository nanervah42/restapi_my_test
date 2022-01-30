from rest_framework import serializers
from django.contrib.auth.models import User
from .models import User


class UserSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'password', 'password2', 'last_name', 'email', 'photo', 'date_of_birth', 'gender')
        read_only_fields = ('id',)
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            photo=validated_data['photo'],
            date_of_birth=validated_data['date_of_birth'],
            gender=validated_data['gender'],
        )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'passwords must match'})
        user.set_password(validated_data['password'])
        user.save()

        return user



# class RegistrationSerializer(serializers.ModelSerializer):
#
#     password2 = serializers.CharField(write_only=True)
#
#     class Meta:
#         model = User
#         fields = ('username', 'password', 'password2', 'first_name', 'last_name', 'email', 'photo', 'date_of_birth', 'gender')
#         extra_kwargs = {
#             'password': {'write_only': True},
#         }
#
#     def save(self):
#         account = User(
#             username=self.validated_data['username'],
#             email=self.validated_data['email'],
#             first_name=self.validated_data['first_name'],
#             date_of_birth=self.validated_data['date_of_birth'],
#             last_name=self.validated_data['last_name'],
#             gender=self.validated_data['gender'],
#             photo=self.validated_data['photo']
#         )
#         password = self.validated_data['password']
#         password2 = self.validated_data['password2']
#
#         if password != password2:
#             raise serializers.ValidationError({'password': 'passwords must match'})
#         account.set_password(password)
#         account.save()
#         return account
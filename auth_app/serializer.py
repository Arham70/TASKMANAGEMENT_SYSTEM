from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import authenticate


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', "is_superuser"]

    def create(self, validated_data):
        # Hash the password before saving
        validated_data['password'] = make_password(validated_data.get('password'))
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # Hash the password before saving
        validated_data['password'] = make_password(validated_data.get('password'))
        return super().update(instance, validated_data)
# class CustomUserSerializer1(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)
#
#     class Meta:
#         model = CustomUser
#         fields = ('email', 'password')
#
#     def login(self):
#         email = self.validated_data['email']
#         password = self.validated_data['password']
#         user = authenticate(email=email, password=password)
#         return user

from dataclasses import fields
import imp
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model

class ReadUserSerializer(serializers.ModelSerializer):
    full_name  = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']

    def get_full_name(self, obj):
        return f'{obj.first_name} {obj.last_name}'

# class RegisterUserSerializer(serializers.ModelSerializer):

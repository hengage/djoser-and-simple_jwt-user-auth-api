from rest_framework import serializers
from django.contrib.auth import get_user_model

from djoser.serializers import UserCreateSerializer

User = get_user_model()

class ReadUserSerializer(serializers.ModelSerializer):
    full_name  = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'full_name']

    def get_full_name(self, obj):
        return f'{obj.first_name} {obj.last_name}'


class UserRegistrationSerializer(serializers.ModelSerializer):
    # Model Serializer that serializes data from the registeration route
    confirm_password = serializers.CharField(
        style={"input_type": "password"},
        write_only=True,
    )

    class Meta:
        model = User
        fields = [
            "email",
            "first_name",
            "last_name",
            "password",
            "confirm_password",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def save(self):

        email = self.validated_data["email"]
        first_name = self.validated_data["first_name"]
        last_name = self.validated_data["last_name"]
        new_user = User(
            email=email,
            first_name=first_name,
            last_name=last_name,
        )

        password = self.validated_data["password"]
        confirm_password = self.validated_data["confirm_password"]

        if password != confirm_password:
            raise serializers.ValidationError(
                {"password": "Passwords must match"}, code="authorization"
            )  # checks to validate password inputed by client
        else:
            new_user.set_password(password)
            new_user.save()
            return new_user

# class RegisterUserSerializer(serializers.ModelSerializer):

from rest_framework import serializers
from .models import UserDetails


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = ("name", "email", "phone_number", "message")

    def create(self, validated_data):
        return UserDetails.objects.create(**validated_data)
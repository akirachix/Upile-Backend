from rest_framework import serializers
from users.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    # officers = PoliceOfficerSerializer(many=True, read_only=True)
    class Meta:
        model = CustomUser
        fields = "__all__"


class MinimalCustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["user_id", "role"]

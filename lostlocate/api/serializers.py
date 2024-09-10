from rest_framework import serializers
from users.models import CustomUser
from next_of_kin.models import NextOfKin  
from unidentified_bodies.models import UnidentifiedBody  


class CustomUserSerializer(serializers.ModelSerializer):
    # officers = PoliceOfficerSerializer(many=True, read_only=True)
    class Meta:
        model = CustomUser
        fields = "__all__"


class MinimalCustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["user_id", "role"] 


"""Serializer for the NextOfKin model & UnidentifiedBody model"""
class NextOfKinSerializer(serializers.ModelSerializer):
    class Meta:
        model = NextOfKin  
        fields = '__all__'  

class UnidentifiedBodySerializer(serializers.ModelSerializer):
    class Meta:
        model = UnidentifiedBody  
        fields = "__all__"  

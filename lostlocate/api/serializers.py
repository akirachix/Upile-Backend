from rest_framework import serializers  
from next_of_kin.models import NextOfKin  
from unidentified_bodies.models import UnidentifiedBody  

"""Serializer for the NextOfKin model & UnidentifiedBody model"""
class NextOfKinSerializer(serializers.ModelSerializer):
    class Meta:
        model = NextOfKin  
        fields = '__all__'  

class UnidentifiedBodySerializer(serializers.ModelSerializer):
    class Meta:
        model = UnidentifiedBody  
        fields = "__all__"  

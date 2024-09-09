from rest_framework import serializers
from missing_persons.models import MissingPerson


"""Serializer class to handle full representation of MissingPerson model"""

class MissingPersonSerializer(serializers.ModelSerializer):
    class Meta:
        """Define which model this serializer is associated with"""
        model = MissingPerson
        """Include all fields of the model in the serialized output"""
        fields = "__all__"

""" Serializer class to handle a minimal representation of MissingPerson model"""
class MinimalMissingPersonSerializer(serializers.ModelSerializer):
    class Meta:
        """ Define which model this serializer is associated with"""
        model = MissingPerson
        """Include only specific fields ('name' and 'age') in the serialized output"""
        fields = ["name", "age"]

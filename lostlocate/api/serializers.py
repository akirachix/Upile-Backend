from rest_framework import serializers  # Importing serializers from Django REST framework
from next_of_kin.models import NextOfKin  # Importing the NextOfKin model
from unidentified_bodies.models import UnidentifiedBody  # Importing the UnidentifiedBody model

# Serializer for the NextOfKin model
class NextOfKinSerializer(serializers.ModelSerializer):
    class Meta:
        model = NextOfKin  # Specify the model to be serialized
        fields = '__all__'  # Include all fields from the model

# Serializer for the UnidentifiedBody model
class UnidentifiedBodySerializer(serializers.ModelSerializer):
    class Meta:
        model = UnidentifiedBody  # Specify the model to be serialized
        fields = "__all__"  # Include all fields from the model

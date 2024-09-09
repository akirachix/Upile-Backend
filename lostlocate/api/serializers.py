from rest_framework import serializers
from mortuary_staff.models import MortuaryStaff

class MortuaryStaffSerializer(serializers.ModelSerializer):
    """
    Serializer for the MortuaryStaff model that includes all fields.
    """
    class Meta:
        model = MortuaryStaff
        # Include all fields from the MortuaryStaff model
        fields = "__all__"

class MinimalMortuaryStaffSerializer(serializers.ModelSerializer):
    """
    Serializer for the MortuaryStaff model that includes only a subset of fields.
    """
    class Meta:
        model = MortuaryStaff
        # Specify which fields to include in the serialized output
        fields = ["name", "location"]

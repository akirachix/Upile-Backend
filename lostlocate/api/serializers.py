from rest_framework import serializers
from mortuary_staff.models import MortuaryStaff

class MortuaryStaffSerializer(serializers.ModelSerializer):
    """
    Serializer for the MortuaryStaff model that includes all fields.
    """
    class Meta:
        model = MortuaryStaff
        fields = "__all__"

class MinimalMortuaryStaffSerializer(serializers.ModelSerializer):
    """
    Serializer for the MortuaryStaff model that includes only a subset of fields.
    """
    class Meta:
        model = MortuaryStaff
        fields = ["name", "location"]

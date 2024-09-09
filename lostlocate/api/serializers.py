from rest_framework import serializers
from police.models import PoliceOfficer
from mortuary.models import Mortuary
from stations.models import PoliceStation


# Serializer for PoliceStation model
class PoliceStationSerializer(serializers.ModelSerializer):
    # officers = PoliceOfficerSerializer(many=True, read_only=True)
    class Meta:
        model = PoliceStation
        fields = "__all__"


# Serializer for Mortuary model
class MortuarySerializer(serializers.ModelSerializer):
    # staff = MortuaryStaffSerializer(many=True, read_only=True)
    class Meta:
        model = Mortuary
        fields = "__all__"



# Serializer for PoliceOfficer model
class PoliceOfficerSerializer(serializers.ModelSerializer):
    # user = MinimalUserSerializer()
    class Meta:
        model = PoliceOfficer
        fields = "__all__"

from rest_framework import serializers
from mortuary_staff.models import MortuaryStaff
from police.models import PoliceOfficer
from mortuary.models import Mortuary
from stations.models import PoliceStation


class MortuaryStaffSerializer(serializers.ModelSerializer):
    user = MinimalUserSerializer()
    class Meta:
        model = MortuaryStaff
        fields = "__all__"
class MortuarySerializer(serializers.ModelSerializer):
    staff = MortuaryStaffSerializer(many=True, read_only=True)
    class Meta:
        model = Mortuary
        fields = "__all__"



class PoliceStationSerializer(serializers.ModelSerializer):
    officers = PoliceOfficerSerializer(many=True, read_only=True)
    class Meta:
        model = PoliceStation
        fields = "__all__"
class MinimalPoliceStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoliceStation
        fields = ["id", "name", "location"]



class MortuarySerializer(serializers.ModelSerializer):
    staff = MortuaryStaffSerializer(many=True, read_only=True)
    class Meta:
        model = Mortuary
        fields = "__all__"
class MinimalMortuarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Mortuary
        fields = ["id", "name", "location"]



class PoliceOfficerSerializer(serializers.ModelSerializer):
    user = MinimalUserSerializer()
    class Meta:
        model = PoliceOfficer
        fields = "__all__"
class MinimalPoliceOfficerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoliceOfficer
        fields = ["id", "badge_number", "rank"]
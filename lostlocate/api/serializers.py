from rest_framework import serializers
from police.models import PoliceOfficer
from mortuary.models import Mortuary
from stations.models import PoliceStation
from mortuary_staff.models import MortuaryStaff
from users.models import CustomUser
from next_of_kin.models import NextOfKin  
from unidentified_bodies.models import UnidentifiedBody 



"""Serializer for PoliceStation model"""
class PoliceStationSerializer(serializers.ModelSerializer):
    # officers = PoliceOfficerSerializer(many=True, read_only=True)
    class Meta:
        model = PoliceStation
        fields = "__all__"


class MortuaryStaffSerializer(serializers.ModelSerializer):
    """
    Serializer for the MortuaryStaff model that includes all fields.
    """
    class Meta:
        model = MortuaryStaff
        fields = "__all__"

class MinimalMortuaryStaffSerializer(serializers.ModelSerializer):
    """db.sqlite3
    Serializer for the MortuaryStaff model that includes only a subset of fields.
    """
    class Meta:
        model = MortuaryStaff
        fields = ["name", "location"]

class MinimalCustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["user_id", "role"] 


"""Serializer for Mortuary model"""
class MortuarySerializer(serializers.ModelSerializer):
    staff = MortuaryStaffSerializer(many=True, read_only=True)
    class Meta:
        model = Mortuary
        fields = "__all__"

"""Serializer for PoliceOfficer model"""
class PoliceOfficerSerializer(serializers.ModelSerializer):
    user = MinimalCustomUserSerializer()
    class Meta:
        model = PoliceOfficer
        fields = "__all__"


class CustomUserSerializer(serializers.ModelSerializer):
    officers = PoliceOfficerSerializer(many=True, read_only=True)
    class Meta:
        model = CustomUser
        fields = "__all__"




"""Serializer for the NextOfKin model & UnidentifiedBody model"""
class NextOfKinSerializer(serializers.ModelSerializer):
    class Meta:
        model = NextOfKin  
        fields = '__all__'  

class UnidentifiedBodySerializer(serializers.ModelSerializer):
    class Meta:
        model = UnidentifiedBody  
        fields = "__all__"  

from rest_framework import serializers
from mortuary.models import Mortuary, MortuaryStaff


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
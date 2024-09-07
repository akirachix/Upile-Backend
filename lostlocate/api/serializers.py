from rest_framework import serializers
from missing_persons.models import MissingPerson


class MissingPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = MissingPerson
        fields = "__all__"
class MinimalMissingPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = MissingPerson
        fields = ["name", "age"]
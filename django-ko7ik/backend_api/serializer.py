from rest_framework import serializers
from .models import *


class SearchDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchData
        fields = "__all__"


class FoundDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoundData
        fields = "__all__"


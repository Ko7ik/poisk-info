from rest_framework import serializers
from .models import *


class VkParserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = VkParserData
        fields = "__all__"


class TaskUrlGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('url_group', )


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class FoundDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoundData
        fields = "__all__"

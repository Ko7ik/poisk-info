from rest_framework import serializers
from .models import *


class TaskSerializer(serializers.ModelSerializer):
    social_net = serializers.SlugRelatedField(slug_field="name", read_only=True)
    vk_parser_data_id = serializers.SlugRelatedField(slug_field="login", read_only=True)
    status = serializers.SlugRelatedField(slug_field="status", read_only=True)

    class Meta:
        model = Task
        fields = "__all__"


class FoundDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoundData
        fields = "__all__"


class VKParserSerializers(serializers.ModelSerializer):
    class Meta:
        model = VkParserData
        fields = "__all__"

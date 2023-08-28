# -*- coding: utf-8 -*-

from rest_framework import serializers, generics
from .models import *

from rest_framework import serializers


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'social_net', 'url_group', 'search_text', 'user_id', 'id_last_post']

    def create(self, validated_data):
        validated_data['user_id'] = self.context['request'].user
        return super().create(validated_data)


class FoundDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoundData
        fields = "__all__"


class VKParserSerializers(serializers.ModelSerializer):
    class Meta:
        model = VkParserData
        fields = "__all__"

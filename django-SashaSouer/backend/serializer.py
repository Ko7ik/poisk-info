from rest_framework import serializers
from backend.models import *



class TaskSerializer(serializers.ModelSerializer):
    # social_net = serializers.StringRelatedField(required=False)
    # social_net = serializers.SlugRelatedField(slug_field='name', queryset=SocialNetwork.objects.all())
    status = serializers.StringRelatedField()

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
        fields = ['id_data', 'login', 'password']


class StatusSerializers(serializers.ModelSerializer):
    class Meta:
        model = StatusTask
        fields = ['id_status', 'status']

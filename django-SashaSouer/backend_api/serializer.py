from rest_framework import serializers
from .models import *
import json



class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"


class FoundDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoundData
        fields = "__all__"

class Login(serializers.ModelSerializer):
    class Meta:
        model = VkParserData
        fields = ('login', )

class Password(serializers.ModelSerializer):
    class Meta:
        model = VkParserData
        fields = ('password',)

class URl(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('url_group',)
class LastPost(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id_last_post',)
class Search(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('search_text',)

class TaskId(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id',)







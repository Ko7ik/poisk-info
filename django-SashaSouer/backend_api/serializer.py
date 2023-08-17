from rest_framework import serializers
from .models import *


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"

class FoundDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoundData
        fields = "__all__"

<<<<<<< Updated upstream
=======

>>>>>>> Stashed changes
class VKParserSerializers(serializers.ModelSerializer):
    class Meta:
        model = VkParserData
        fields = "__all__"
<<<<<<< Updated upstream







=======
>>>>>>> Stashed changes

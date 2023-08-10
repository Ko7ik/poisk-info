from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from .models import search_data
from .models import found_data



class SearchSerializer(serializers.Serializer):
        url_groupe = serializers.URLField()
        search_text = serializers.CharField()

class FoundSerializer(serializers.Serializer):
        url_groupe = serializers.URLField()
        date_time = serializers.DateTimeField(read_only=True)
        found_text = serializers.CharField()




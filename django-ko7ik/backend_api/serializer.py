from rest_framework import serializers
from .models import *


class FoundDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = found_data
        fields = ['url_groupe', 'date', 'found_text']


class SearchDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = search_data
        fields = ['url_groupe', 'search_string']
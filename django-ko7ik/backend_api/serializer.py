from rest_framework import serializers
from .models import *


class FoundDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoundData
        fields = ['url_group', 'date', 'found_text']


class SearchDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchData
        fields = ['url_group', 'search_string']
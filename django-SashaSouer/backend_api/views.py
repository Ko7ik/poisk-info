from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import search_data
from .models import found_data
from .serializer import SearchSerializer
from .serializer import FoundSerializer

class SearchAPIView(APIView):
    def post(self, request):
        serializer = SearchSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data_new = search_data.objects.create(
        url_groupe=request.data['url_groupe'],
        search_text=request.data['search_text']
        )
        return Response({'data' : model_to_dict(data_new).data})
class FoundAPIView(APIView):
    def get(self, request):
        f = found_data.objects.all()
        return Response({'data': FoundSerializer(f, many=True).data})


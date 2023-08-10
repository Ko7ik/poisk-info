from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from .serializer import *
from rest_framework.response import Response


class FoundDataView(APIView):
    def get(self, request):
        output = [
            {
                "url_groupe": output.url_groupe,
                "date": output.date,
                "found_text": output.found_text
            } for output in found_data.objects.all()
        ]
        return Response(output)

    def post(self, request):
        serializer = FoundDataSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


class SearchDataView(APIView):
    def get(self, request):
        output = [
            {
                "url_groupe": output.url_groupe,
                "search_string": output.search_string
            } for output in search_data.objects.all()
        ]
        return Response(output)

    def post(self, requset):
        serializer = SearchDataSerializer(data=requset.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

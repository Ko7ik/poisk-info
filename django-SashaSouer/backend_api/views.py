from rest_framework.views import APIView
from .serializer import *
from rest_framework.response import Response
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>MAIN PAGE</h1>")


class FoundDataView(APIView):
    def get(self, request):
        queryset = FoundData.objects.all()
        serializer = FoundDataSerializer(instance=queryset, many=True)
        return Response({'data': serializer.data})

    def post(self, request):
        serializer = FoundDataSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


class SearchDataView(APIView):
    def get(self, request):
        queryset = SearchData.objects.all()
        serializer = SearchDataSerializer(instance=queryset, many=True)
        return Response({'data': serializer.data})

    def post(self, request):
        serializer = SearchDataSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

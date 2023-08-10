from rest_framework.views import APIView
from .serializer import *
from rest_framework.response import Response


class FoundDataView(APIView):
    def get(self, request):
        queryset = found_data.objects.all()
        serializer = FoundDataSerializer(instance=queryset, many=True)
        return Response({'data': serializer.data})

    def post(self, request):
        serializer = FoundDataSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


class SearchDataView(APIView):
    def get(self, request):
        queryset = search_data.objects.all()
        serializer = SearchDataSerializer(instance=queryset, many=True)
        return Response({'data': serializer.data})

    def post(self, request):
        serializer = SearchDataSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

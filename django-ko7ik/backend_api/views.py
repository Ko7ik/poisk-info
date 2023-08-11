from rest_framework import generics
from rest_framework.views import APIView
from .serializer import *
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticatedOrReadOnly


# ------------ Главная страница ------------


def index(request):
    return render(request, 'backend_api/index.html')

# ------------ SearchDATA запросы ------------


# class SearchDataView(APIView):
#
#     def get(self, request):
#         queryset = SearchData.objects.all()
#         serializer = SearchDataSerializer(instance=queryset, many=True)
#         return Response({'data': serializer.data})
#
#     def post(self, request):
#         serializer = SearchDataSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)

# Заменяем APIView на класс generic


class SearchDataList(generics.ListCreateAPIView):
    queryset = SearchData.objects.all()
    serializer_class = SearchDataSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class SearchDataDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SearchData.objects.all()
    serializer_class = SearchDataSerializer


# ------------ FoundDATA запросы ------------

# class FoundDataView(APIView):
#     def get(self, request):
#         queryset = FoundData.objects.all()
#         serializer = FoundDataSerializer(instance=queryset, many=True)
#         return Response({'data': serializer.data})
#     permission_classes = (IsAuthenticatedOrReadOnly, )
#
#     def post(self, request):
#         serializer = FoundDataSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#         try:
#             instance = FoundData.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exists"})
#         serializer = FoundDataSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})

# Заменяем APIView на класс generic

class FoundDataList(generics.ListCreateAPIView):
    queryset = FoundData.objects.all()
    serializer_class = FoundDataSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class FoundDataDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FoundData.objects.all()
    serializer_class = FoundDataSerializer




from rest_framework import generics
from rest_framework.views import APIView
from .serializer import *
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated


# ------------ Главная страница ------------

def index(request):
    return render(request, 'backend_api/index.html')


# ------------ SearchDATA запросы ------------

class SearchDataList(generics.ListCreateAPIView):
    queryset = SearchData.objects.all()
    serializer_class = SearchDataSerializer
    permission_classes = (IsAuthenticated, )


class SearchDataUpdate(generics.RetrieveUpdateAPIView):
    queryset = SearchData.objects.all()
    serializer_class = SearchDataSerializer
    permission_classes = (IsAuthenticated, )


class SearchDataDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = SearchData.objects.all()
    serializer_class = SearchDataSerializer
    permission_classes = (IsAuthenticated, )


# ------------ FoundDATA запросы ------------

class FoundDataList(generics.ListCreateAPIView):
    queryset = FoundData.objects.all()
    serializer_class = FoundDataSerializer
    #permission_classes = (IsAuthenticated, )


class FoundDataUpdate(generics.RetrieveUpdateAPIView):
    queryset = FoundData.objects.all()
    serializer_class = FoundDataSerializer
    permission_classes = (IsAuthenticated, )


class FoundDataDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = FoundData.objects.all()
    serializer_class = FoundDataSerializer
    permission_classes = (IsAuthenticated, )

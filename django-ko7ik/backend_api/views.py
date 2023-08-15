from rest_framework import generics
from rest_framework.views import APIView
from .serializer import *
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated


# ------------ Главная страница ------------

def index(request):
    return render(request, 'backend_api/index.html')


# ------------ Task запросы ------------
class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    # permission_classes = (IsAuthenticated, )


class TaskUpdate(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    # permission_classes = (IsAuthenticated, )


class TaskDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    # permission_classes = (IsAuthenticated, )


# ------------ FoundDATA запросы ------------

class FoundDataList(generics.ListCreateAPIView):
    queryset = FoundData.objects.all()
    serializer_class = FoundDataSerializer
    # permission_classes = (IsAuthenticated, )


class FoundDataUpdate(generics.RetrieveUpdateAPIView):
    queryset = FoundData.objects.all()
    serializer_class = FoundDataSerializer
    # permission_classes = (IsAuthenticated, )


class FoundDataDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = FoundData.objects.all()
    serializer_class = FoundDataSerializer
    # permission_classes = (IsAuthenticated, )

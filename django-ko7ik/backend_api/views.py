from rest_framework import generics
from rest_framework.views import APIView
from .serializer import *
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django.http import JsonResponse


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


def serialize_and_save_to_json(request):
    serialized_vk_data = VKParserSerializers(VkParserData.objects.all(), many=True).data
    serialized_task_data = TaskSerializer(Task.objects.all(), many=True).data
    data_for_json = {
        "vk": {
            "auth":
                {
                    "login": serialized_vk_data[0]['login'],
                    "password": serialized_vk_data[0]['password']
                },
            "urls": {
                "feed": serialized_task_data[0]['url_group'],
                "login": "https://vk.com/login"
            },
            "task": {
                "id_last_post": serialized_task_data[0]['id_last_post'],
                "text": serialized_task_data[0]['search_text'],
                "id_task": serialized_task_data[0]['id']
            }
        }
    }

    return JsonResponse(data_for_json, status=200, safe=False)

import json

from django.http import JsonResponse
from rest_framework import generics
from .serializer import *
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated


# ------------ Главная страница ------------

def index(request):
    return render(request, 'backend_api/index.html')


def serialize_and_save_to_json(request):
    vk_parser_data = VkParserData.objects.all()
    # task_data = SocialNetwork.objects.all()

    serialized_vk_parser_data = VkParserDataSerializer(vk_parser_data, many=True).data
    url_group = TaskUrlGroupSerializer(vk_parser_data).data

    data_for_json = {
      "vk" : {
        "auth" : serialized_vk_parser_data,
        "urls" : {
          "feed" : url_group,
          "login" : "https://vk.com/login"
        },
        "task" : {
          "id_last_post" : 938933991654215,
          "text" : "test-text"
        }
      }
    }
    with open('config.example.json', 'w') as json_file:
        json.dump(data_for_json, json_file, indent=4)
    return JsonResponse({'message': 'Data serialized and saved to JSON file.'}, status=200)


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

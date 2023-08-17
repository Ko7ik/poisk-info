from rest_framework import generics
from rest_framework.views import APIView
from .serializer import *
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django.http import JsonResponse


# ------------ Главная страница ------------ #

def index(request):
    return render(request, 'backend_api/index.html')



# ------------ Task запросы ------------
class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated, )


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
    VkObject = VkParserData.objects.all()
    TaskObject = Task.objects.all()
    serializers_URL = TaskSerializer(TaskObject, many=True).data
    serializers_LastPost = TaskSerializer(TaskObject, many=True).data
    serializers_Search = TaskSerializer(TaskObject, many=True).data
    serialized_login = VKParserSerializers(VkObject, many=True).data
    serialized_password = VKParserSerializers(VkObject, many=True).data
    serialized_id_task = TaskSerializer(TaskObject, many=True).data

    data_for_json = {
      "vk" : {
        "auth" :
            {
                "login": serialized_login[0]['login'],
                "password":serialized_password[0]['password']
            },
        "urls" : {
          "feed" : serializers_URL[0]['url_group'],
          "login" : "https://vk.com/login"
        },
        "task" : {
            "id_last_post" : serializers_LastPost[0]['id_last_post'],
            "text" : serializers_Search[0]['search_text'],
            "id_task": serialized_id_task[0]['id']
        }
      }
    }

    with open('config.example.json', 'w',encoding='utf-8') as json_file:
        json.dump(data_for_json, json_file, indent=4,ensure_ascii=False)

    return JsonResponse(data_for_json, status=200)

    # {'message': 'Data serialized and saved to JSON file.'}


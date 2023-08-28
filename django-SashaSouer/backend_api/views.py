# -*- coding: utf-8 -*-
import subprocess
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets, status, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializer import *


# Отображение главной страницы
def index(request):
    return render(request, 'backend_api/index.html')


# Проверка на валидность токена
@api_view(['GET'])
def validate_token(request):
    return Response({'message': 'Token is valid'})


# Код для запуска парсера
@api_view(['POST'])
def parser_run(request):
    script_path = 'parser/main.py'
    subprocess.call(['python', script_path])
    return Response({'message': 'Parser started successfully'})


# Создание JSON для парсера
def create_json_response_to_parser(request):
    serialized_vk_data = VKParserSerializers(VkParserData.objects.all(), many=True).data
    serialized_task_data = TaskSerializer(Task.objects.all(), many=True).data
    data_for_json_array = []
    for i in range(len(Task.objects.all())):
        data_for_json = {
            "vk": {
                "auth":
                    {
                        "login": serialized_vk_data[0]['login'],
                        "password": serialized_vk_data[0]['password']
                    },
                "urls": {
                    "feed": serialized_task_data[i]['url_group'],
                    "login": "https://vk.com/login"
                },
                "task": {
                    "id_last_post": serialized_task_data[i]['id_last_post'],
                    "text": serialized_task_data[i]['search_text'],
                    "id_task": serialized_task_data[i]['id']
                }
            }
        }
        data_for_json_array.append(data_for_json)
    return JsonResponse(data_for_json_array, status=200, safe=False)

    # {'message': 'Data serialized and saved to JSON file.'}

# Выдать пользователю токен при аутентификации
class UserTokenView(APIView):
    def get(self, request):
        user = request.user
        tokens = Token.objects.filter(user=user)
        data = [{'id': token.user.id, 'token': token.key} for token in tokens]
        return Response(data)


# Views для Task
class TaskViewSet(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    # permission_classes = [IsAuthenticated]  # Проверка аутентификации

    # Присваиваем ID для социальной сети по её названию
    def create(self, request, *args, **kwargs):
        social_net = request.data.get('social_net')
        if social_net == 'Вконтакте':
            request.data['social_net'] = 1
        elif social_net == 'Telegram':
            request.data['social_net'] = 2
        return super().create(request, *args, **kwargs)

    # def get_queryset(self):
    #     # Получаем текущего аутентифицированного пользователя
    #     username = self.request.username
    #     # Фильтруем задачи по пользователю
    #     queryset = Task.objects.filter(username=username)
    #     return queryset
    #
    # def perform_create(self, serializer):
    #     # Присваиваем текущего аутентифицированного пользователя полю "user_id"
    #     serializer.save(username=self.request.username)


# Views для редактирования Task
class TaskViewSetDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]  # Проверка аутентификации


# Views для FoundData
class FoundDataViewSet(viewsets.ModelViewSet):
    queryset = FoundData.objects.all()
    serializer_class = FoundDataSerializer

    #  Проверка на тип данных, на случай, если придет list
    def create(self, request, *args, **kwargs):
        if isinstance(request.data, list):
            serializer = self.get_serializer(data=request.data, many=True)
        else:
            serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

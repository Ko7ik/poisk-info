# -*- coding: utf-8 -*-
from django.shortcuts import render
from rest_framework import viewsets, status, generics
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .service import *

# from .rabbitmq_publisher import send_message
from .serializer import *


# Отображение страницы бэкенда DRF
def index(request):
    return render(request, 'backend_api/index.html')


# Проверка на валидность токена
@api_view(['GET'])
def validate_token(request):
    return Response({'message': 'Token is valid'})


# # Код для запуска парсера
# @api_view(['POST'])
# def parser_run(request):
#     script_path = 'parser/main.py'
#     subprocess.call(['python', script_path])
#     return Response({'message': 'Parser started successfully'})


# # Создание JSON для аутентификации парсера
# def create_json_data_to_login():
#     # сериализация для создания JSON
#     serialized_task_data = TaskSerializer(Task.objects.all(), many=True).data
#     serialized_vk_data = VKParserSerializers(VkParserData.objects.all(), many=True).data
#     # цикл для создания JSON
#     for i in range(len(Task.objects.all())):
#         data_for_login = {
#             "auth":
#                 {
#                     "login": serialized_vk_data[int(serialized_task_data[i]['vk_parser_data_id']) - 1]['login'],
#                     "password": serialized_vk_data[int(serialized_task_data[i]['vk_parser_data_id']) - 1]['password']
#                 }
#         }
#         # Отправка данных через RabbitMQ
#         send_message(data_for_login)
#         print('item ' + str(i) + ' - данные для аутентификации отправлены в очередь')
#
#
# # Создание JSON для цели парсера (Вконтакте)
# def create_json_response_to_parser():
#     # сериализация для создания JSON
#     serialized_task_data = TaskSerializer(Task.objects.all(), many=True).data
#     serialized_status_data = StatusSerializers(StatusTask.objects.all(), many=True).data
#     # цикл для создания JSON
#     for i in range(len(Task.objects.all())):
#         data_for_pars = {
#             "vk": {
#                 "urls": {
#                     "feed": serialized_task_data[i]['url_source'],
#                     "login": "https://vk.com/login"
#                 },
#                 "task": {
#                     "id_last_post": serialized_task_data[i]['id_last_post'],
#                     "text": serialized_task_data[i]['search_text'],
#                     "id_task": serialized_task_data[i]['id'],
#                     "status": serialized_status_data[0]['id']
#                 }
#             }
#         }
#         # Отправка данных через RabbitMQ
#         send_message(data_for_pars)
#         print('item ' + str(i) + ' - данные для цели парсера отправлены в очередь')


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
    # permission_classes = [IsAuthenticated]  # Проверка аутентификации


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

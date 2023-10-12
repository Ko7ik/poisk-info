from django.shortcuts import render
from rest_framework import generics, viewsets, status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.serializer import *
from backend.models import *


# Отображение главной страницы
def index(request):
    return render(request, 'backend/index.html')


# Проверка на валидность токена
@api_view(['GET'])
def validate_token(request):
    return Response({'message': 'Token is valid'})


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


# Views для редактирования Task
class TaskViewSetDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    # permission_classes = [IsAuthenticated]  # Проверка аутентификации


# Views для FoundData
class FoundDataViewSet(generics.ListCreateAPIView):
    queryset = FoundData.objects.all()
    serializer_class = FoundDataSerializer

    # permission_classes = [IsAuthenticated]  # Проверка аутентификации

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


class FoundDataViewSetDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FoundData.objects.all()
    serializer_class = FoundDataSerializer
    # permission_classes = [IsAuthenticated]  # Проверка аутентификации

# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from celery import shared_task
import json

from backend_api.models import Task, VkParserData, StatusTask
from backend_api.serializer import TaskSerializer, VKParserSerializers, StatusSerializers
from backend_api import rabbitmq_consumer


# @shared_task
# def process_login_data():
#     # Ваш код для создания JSON данных аутентификации парсера
#
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
#         rabbitmq_consumer.send_message(data_for_login)
#         print('Данные для аутентификации отправлены в очередь')


@shared_task
def process_parser_data():
    # Ваш код для создания JSON данных цели парсера

    # сериализация для создания JSON
    serialized_vk_data = VKParserSerializers(VkParserData.objects.all(), many=True).data
    serialized_task_data = TaskSerializer(Task.objects.all(), many=True).data
    serialized_status_data = StatusSerializers(StatusTask.objects.all(), many=True).data
    # цикл для создания JSON
    for i in range(len(Task.objects.all())):
        data_for_pars = {
            "vk": {
                "auth": {
                    "login": serialized_vk_data[int(serialized_task_data[i]['vk_parser_data_id']) - 1]['login'],
                    "password": serialized_vk_data[int(serialized_task_data[i]['vk_parser_data_id']) - 1]['password']
                },
                "urls": {
                    "feed": serialized_task_data[i]['url_source'],
                    "login": "https://vk.com/login"
                },
                "task": {
                    "id_last_post": serialized_task_data[i]['id_last_post'],
                    "text": serialized_task_data[i]['search_text'],
                    "id_task": serialized_task_data[i]['id_task_name'],
                    "status": serialized_status_data[0]['id_status']
                }
            }
        }
        # Отправка данных через RabbitMQ
        # json_string = json.dumps(data_for_pars)
        rabbitmq_consumer.send_message(data_for_pars)
        print('item ' + str(i) + ' - данные для цели парсера отправлены в очередь')
    return print("УСПЕШНЫЙ УСПЕХ")

# celery -A config worker -l info --pool=solo

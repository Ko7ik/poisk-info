# -*- coding: utf-8 -*-
import json

import pika
from parser.src.VkDriverTools import VkDriverTools

flag = 0


def send_message(data):
    # Подключение к RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    # Определение очереди
    channel.queue_declare(queue='parser_queue')

    # Отправка сообщения
    channel.basic_publish(exchange='', routing_key='parser_queue', body=data)

    # Закрытие соединения
    connection.close()


def callback(ch, method, properties, body):
    # Ваш код для обработки полученных сообщений и выполнения парсинга
    message = json.loads(body)
    print(message)
    # print(" [x] Received message from parser_queue:", message)
    global flag
    # Добавьте вашу логику обработки полученных данных здесь
    vkDriverTools = VkDriverTools()
    vkDriverTools.raschlenenka(message)  # Получение POST
    print("Парсер: - Получил данные")
    if flag == 0:
        vkDriverTools.login()  # Авторизация
        print("Парсер: - Авторизовался")
        flag = 1
    if vkDriverTools.vk_last_id == 0:  # Проверка на обрабатывалась ли страница
        print("Парсер: - Выбрал get_start")
        vkDriverTools.get_start()  # Запуск парсера на обработку с первой записи
    else:
        print("Парсер: - Выбрал get_feed")
        vkDriverTools.get_feed()  # Запуск парсера на обработку с последней найденной записи
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print("Received message: %r" % body)
    return message


def consume_messages():
    # Подключение к RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    # Определение очереди
    channel.queue_declare(queue='parser_queue')

    # Установка функции обратного вызова для обработки полученных сообщений
    channel.basic_consume(queue='parser_queue', on_message_callback=callback, auto_ack=True)

    # Начало прослушивания очереди
    print('Waiting for messages...')
    channel.start_consuming()

# from parser.src.VkDriverTools import VkDriverTools
# import time
# import pika
# import json
#
#
# flag = 0
#
#
# # consumer
#
# def callback(ch, method, properties, body):
#     message = json.loads(body)
#     print(" [x] Received message from parser_queue:", message)
#     global flag
#     # Добавьте вашу логику обработки полученных данных здесь
#     vkDriverTools.raschlenenka(message)  # Получение POST
#     print("Парсер: - Получил данные")
#     if flag == 0:
#             vkDriverTools.login()  # Авторизация
#             print("Парсер: - Авторизовался")
#             flag = 1
#     if vkDriverTools.vk_last_id == 0:  # Проверка на обрабатывалась ли страница
#             print("Парсер: - Выбрал get_start")
#             vk = vkDriverTools.get_start  # Запуск парсера на обработку с первой записи
#     else:
#             print("Парсер: - Выбрал get_feed")
#             vk = vkDriverTools.get_feed  # Запуск парсера на обработку с последней найденной записи
#     ch.basic_ack(delivery_tag=method.delivery_tag)
#     return message
#
#
# def consume_messages():
#     connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
#     channel = connection.channel()
#
#     channel.queue_declare(queue='parser_queue')
#     channel.basic_qos(prefetch_count=1)
#     channel.basic_consume(queue='parser_queue', on_message_callback=callback)
#
#     print(' [*] Waiting for messages. To exit press CTRL+C')
#     channel.start_consuming()
#
#
# vkDriverTools = VkDriverTools()
# consume_messages()
